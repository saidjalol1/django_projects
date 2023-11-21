from datetime import datetime, timedelta
from calendar import monthrange
from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.views import View
from .forms import GroupForm, GroupUpdateForm,PaymentForm
from students.forms import StudentIcedForm
from .models import Group, Room
from teachers.models import Teacher
from students.models import Students, Attandence, Payment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
current_date = datetime.now()
year = datetime.now().year
month = datetime.now().month
def generate_month_dates(year, month, pattern='all'):
    
    first_day = datetime(year, month, 1)

    _, last_day = monthrange(year, month)

    if pattern == 'even':
       month_dates = [first_day + timedelta(days=i * 2) for i in range(last_day // 2)]
    elif pattern == 'uneven':
        month_dates = [first_day + timedelta(days=i * 2 + 1) for i in range(last_day // 2)]
    else:
        month_dates = [first_day + timedelta(days=i) for i in range(last_day)]

    return month_dates

# Example usage:

 # November


# Print the generated dates





class GroupView(View):
    template_name = 'group/group.html'
    form_class = GroupForm
    success_url = reverse_lazy('groups:group_page')
    

    def get_context_data(self, **kwargs):
        if 'form' not in kwargs:
            kwargs['form'] = GroupForm()
        if 'group_update' not in kwargs:
            kwargs['group_update'] = GroupUpdateForm()
        kwargs['groups'] = Group.objects.all()
        kwargs['teachers'] = Teacher.objects.all()
        return kwargs
    def get(self, request,*args,**kwargs):
        context = self.get_context_data()
        if 'filter' in request.GET:
            teacher = request.GET.get('teacher')
            started_date = request.GET.get('started_date')
            ends_in = request.GET.get('ends_in')
            days = request.GET.get('days')
            try:
                if teacher:
                    context['groups']= Group.objects.filter(teacher__name__icontains=teacher)
                elif started_date:
                    context['groups'] = Group.objects.filter(started_date=started_date)
                elif ends_in:
                    context['groups'] = Group.objects.filter(ends_in=ends_in)
                elif days:
                    context['groups'] = Group.objects.filter(days=days)
                else:
                    context['groups'] = Group.objects.all()
                    return render(request,self.template_name,context)
            except:
                return HttpResponse('<h1>Group with those criterias doesn\'t exit</h1>')
        return render(request, self.template_name,context)
    
    def post(self,request, *args, **kwargs):
        ctxt = {}

        if 'group_update' in request.POST:
            form = GroupUpdateForm(request.POST)
            if form.is_valid():
                group = Group.objects.get(id=request.POST.get('group'))
                group.name = request.POST.get('name')
                group.price = request.POST.get('price')
                group.time = request.POST.get('time')
                group.room = Room.objects.get(id=request.POST.get('room'))
                group.days = request.POST.get('days')
                group.teacher = Teacher.objects.get(id=request.POST.get('teacher'))
                group.started_date = request.POST.get('started_date')
                group.ends_in = request.POST.get('ends_in')
                group.save()
            else:
                ctxt['edit_form'] = form
        elif 'create' in request.POST:
            form = GroupForm(request.POST)
            if form.is_valid():
               form.save()
            else:
                ctxt['form'] = form
        if 'delete' in request.POST:
            student = Group.objects.get(id=request.POST.get('gr'))
            print(student)
            student.delete()
      
        return render(request, self.template_name,self.get_context_data(**ctxt))
    # def form_valid(self, form):
    #     object = form.save(commit=False)
    #     time = form.cleaned_data['time']
    #     days = form.cleaned_data['days']
    #     teacher = form.cleaned_data['teacher']
    #     room = form.cleaned_data['room']
    #     try:
    #         availablety_teacher = Group.objects.filter(teacher=teacher).filter(days=days).get(time=time)
    #     except Group.DoesNotExist:
    #         availablety_teacher = None
    #     try:
    #         availablety_room = Group.objects.filter(days=days).get(time=time)
    #     except Group.DoesNotExist:
    #         availablety_room = None
    #     if availablety_teacher:
    #         return HttpResponse("<h1>This Teacher isn't available in this time</h1>")
    #     else:
    #         if availablety_room:
    #             return HttpResponse('<h1>There is a lesson in that Room at this time</h1>')
    #         else:
    #             form.save()
    #     return super().form_valid(form)


class GroupDetailView(View):
    template_name = 'group/group-detail.html'

    def get_object(self):
        try:
            object = Group.objects.get(pk=self.kwargs['pk'])
        except Group.DoesNotExist:
            raise Http404('Question not found!')
        return object
    

    def get_context_data(self, **kwargs):
        kwargs['object'] = self.get_object()
        kwargs['students'] = Students.objects.all()
        kwargs['groups'] = Group.objects.all()
        kwargs['month_name'] = current_date.strftime('%B')
        if self.get_object().days != 'Toq kunlar':
            dates_in_current_month = generate_month_dates(year, month, pattern='uneven')
        elif self.get_object().days == 'Toq kunlar':
            dates_in_current_month = generate_month_dates(year, month, pattern='even')
        else:
            dates_in_current_month = generate_month_dates(year, month)
        kwargs['dates'] = dates_in_current_month
        attandence_list = []
        kwargs['attandence_list'] = attandence_list
        for i in self.get_object().students.all():
            for j in dates_in_current_month:
                # print('==> ', j.date() ) 
                attendance, created = Attandence.objects.get_or_create(
                student=i,
                date_added=j.date(),
                group = self.get_object(),  # Set default values if the object is created
                )
                # print(attendance.status)

                # if created:
                #     print(f"Attendance object created for Student {i} on {j}")
                # else:
                #     print(f"Attendance object already exists for Student {i} on {j}")
                attandence_list.append(attendance)
        if 'student_deactivate' not in kwargs:
            kwargs['student_deactivate'] = StudentIcedForm()
        if 'edit_form' not in kwargs:
            kwargs['edit_form'] = GroupUpdateForm(instance=self.get_object())
        if 'payment_form' not in kwargs:
            kwargs['payment_form'] = PaymentForm()
        return kwargs
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

            
    def post(self, request, *args, **kwargs):
        ctxt = {}
        if 'student_deactivate' in request.POST:
            form = StudentIcedForm(request.POST)
            if form.is_valid():
                instance_student = request.POST.get('student_id')
                print(instance_student)
                student = Students.objects.get(id = instance_student)
                cause = form.cleaned_data['couse_of_status_change']
                status = form.cleaned_data['status']
                date = form.cleaned_data['status_change_date']
                student.couse_of_status_change = cause
                student.status = status
                student.status_change_date = date
                student.save()
                print(student)
                # form.save()
        if 'edit' in request.POST:
            group = self.get_object()
            print(group)
            form = GroupUpdateForm(request.POST, instance=group)
            if form.is_valid():
                form.save()
            else:
                form = GroupUpdateForm()
        if 'student_plus' in request.POST:
            print('tracked')
            student = Students.objects.get(id=request.POST.get('student_add'))
            student.group.add(self.get_object())
            print(student)
        if 'keldi'in request.POST:
            student_instance = request.POST.get('student')
            date = request.POST.get('date')
            date_string = date
            date_object = datetime.strptime(date_string, '%b. %d, %Y')
            formatted_date = date_object.strftime('%Y-%m-%d')
            attandence =  Attandence.objects.get(student_id=student_instance,group = self.get_object(), date_added= formatted_date)
            attandence.status = 1
            attandence.save()
        if 'kelmadi'in request.POST:
            student_instance = request.POST.get('student')
            date = request.POST.get('date')
            date_string = date
            date_object = datetime.strptime(date_string, '%b. %d, %Y')
            formatted_date = date_object.strftime('%Y-%m-%d')
            attandence =  Attandence.objects.get(student_id=student_instance,group = self.get_object(), date_added= formatted_date)
            attandence.status = 0
            attandence.save()
        if 'remove_group' in request.POST:
            student_id = request.POST.get('student_id')
            student = Students.objects.get(id=student_id)
            print(student.group)
            student.group.remove(self.get_object())
            student.save()
        if 'change' in request.POST:
            student_id = request.POST.get('student_id')
            group = Group.objects.get(id = request.POST.get('group'))
            student = Students.objects.get(id=student_id)
            student.group.remove(self.get_object())
            student.group.add(group)
            student.save()
        if 'payment' in request.POST:
            form = PaymentForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                student = form.cleaned_data['student']
                course = form.cleaned_data['course']
                date = form.cleaned_data['date_added']
                try:
                    payment_month = Payment.objects.get(student=student,course=course,date_added__month=date.month)
                    print(date.month ,' =>  ')
                except Payment.DoesNotExist:
                    payment_month = None
                # payment_month = student.payment_set.annotate(month_stamp=Extract('date', 'month')).values_list('month_stamp', flat=True)
                # payment = student.payment_set.get(date__month=current_date.month)
                if payment_month is not None:
                    if payment_month.course == course:
                        return HttpResponse('<h1>This student has already made a payment for this month</h1>')
                elif payment_month == None:
                    form.save()
            else:
                return HttpResponse('<h1>Fill all fields</h1>')
        return render(request, self.template_name, self.get_context_data(**ctxt)) 




