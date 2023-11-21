from typing import Any
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView,CreateView, FormMixin
from django.views.generic import ListView,DetailView 
from .models import Students, Payment
from .forms import StudentsForm, AddToGroupForm, PaymentForm,StudentIcedForm,StudentsUpdateForm
from groups.models import Group
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


@csrf_exempt  # Use this decorator for simplicity; handle CSRF properly in production
def student_filter(request):
    if request.method == 'POST':
        # Get form values from the AJAX request
        student = request.POST.get('student')
        course = request.POST.get('course')
        status = request.POST.get('status')
        economical_status = request.POST.get('economical_status')

        # Your logic here to process the form values

        # Return a JSON response if needed
        return JsonResponse({'message': 'Form values received successfully'})

    return JsonResponse({'message': 'Invalid request method'})

class StudentsView(View):
    template_name = 'students.html'

    def get_context_data(self,**kwargs):
        kwargs['students'] = Students.objects.all()
        kwargs['groups'] = Group.objects.all()
        if 'create_form' not in kwargs:
            kwargs['create_form'] = StudentsForm()
        if 'edit_form' not in kwargs:
            kwargs['edit_form'] = StudentsUpdateForm()
        return kwargs

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        if 'filter' in request.GET:
            by_name = request.GET.get('by_name')
            by_group = request.GET.get('by_group')
            economical_status = request.GET.get('economical_status')
            if by_name:
                context['students'] = Students.objects.filter(name = by_name)
            elif by_group:
                context['students'] =Students.objects.filter(group__name__icontains=by_group)
            elif economical_status:
                context['students'] = Students.objects.filter(economical_status=economical_status)
            else:
                context['students'] = Students.objects.all()
                return render(request, self.template_name,context)
        return render(request, self.template_name,context)


    def post(self, request, *args, **kwargs):
        ctxt = {}

        if 'edit' in request.POST:
            form = StudentsUpdateForm(request.POST)
            if form.is_valid():
                student = Students.objects.get(id=request.POST.get('st'))
                student.name = form.cleaned_data['name']
                student.surname = form.cleaned_data['surname']
                student.phone_number = form.cleaned_data['phone_number']
                student.status = form.cleaned_data['status']
                for i in form.cleaned_data['group']:
                    student.group.add(i)
                
                student.save()
            else:
                ctxt['edit_form'] = form
        elif 'create' in request.POST:
            form = StudentsForm(request.POST)
            if form.is_valid():
               form.save()
            else:
                ctxt['create_form'] = form
        if 'delete' in request.POST:
            student = Students.objects.get(id=request.POST.get('student'))
            print(student)
            student.delete()
      
        return render(request, self.template_name,self.get_context_data(**ctxt))

# class StudentDetailView(FormMixin,DetailView):
#     model = Students
#     template_name = 'second_talaba.html'
#     form_class = AddToGroupForm
#     success_ulr = reverse_lazy('students:students_page')


    
#     def get_success_url(self):
#         return reverse("students:student_detail", kwargs={"pk": self.object.id})

#     extra_context = {
#         'add_to_group_form':AddToGroupForm(),
#         'payment_form' : PaymentForm()
#     }

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context = {
#     #         'payments':Payment.objects.all()
#     #     }
#     #     return context
#     def form_valid(self, form):
#         # object.group.add(obj.group)
#         form.save()
#         return super().form_valid(form)


#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             # name = form.cleaned_data['name']
#             # surname = form.cleaned_data['surname']
#             # phone_number = form.cleaned_data['phone_number']
#             group = form.cleaned_data['group']
#             if group:
#                 student_groups = self.get_object()
#                 for i in group:
#                     student_groups.group.add(i)
#                 else:
#                     return self.form_valid(form)
#         else:
#             return self.form_invalid(form)


class StudentsDetailView(View):
    template_name = 'second_talaba.html'

    def get_object(self):
        try:
            object = Students.objects.get(pk=self.kwargs['pk'])
        except Students.DoesNotExist:
            raise Http404('Question not found!')
        return object

    def get_context_data(self, **kwargs):
        kwargs['object'] = self.get_object()
        if 'payment_form' not in kwargs:
            kwargs['payment_form'] = PaymentForm()
        if 'add_to_group_form' not in kwargs:
            kwargs['add_to_group_form'] = AddToGroupForm()

        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        ctxt = {}

        if 'payment' in request.POST:
            payment_form = PaymentForm(request.POST)

            if payment_form.is_valid():
                payment = Payment.objects.filter(student=self.get_object())
                if payment:
                    ctxt['payment_form'] = payment_form
                else:
                    payment_form.save()
            else:
                ctxt['payment_form'] = payment_form

        elif 'add_group' in request.POST:
            add_to_group_form = AddToGroupForm(request.POST)

            if add_to_group_form.is_valid():
                group = add_to_group_form.cleaned_data['group']
                if group:
                    student_groups = self.get_object()
                    for i in group:
                        student_groups.group.add(i)
                else:
                    ctxt['add_to_group_form'] = add_to_group_form
            else:
                ctxt['add_to_group_form'] = add_to_group_form

        return render(request, self.template_name, self.get_context_data(**ctxt))
    
