import datetime
from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView , FormMixin
from django.utils.text import slugify
from .forms import CourseForm, StudentForm, TeacherForm, AttendanceForm, PaymentForm
from django.db.models.functions import Extract

# from django.dispatch import receiver
# from django.db.models.signals import post_save, post_delete
# from django.template.defaultfilters import slugify


   
# Models
from .models import Student, Teacher, Course, Attendance, Payment

class HomePage(ListView):
    model = Course
    template_name = 'index.html'



class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    success_url =  reverse_lazy('courses:home')


class TeacherHire(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'courses/student_form.html'
   


class AddCourseView(CreateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('courses:home')

    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = slugify(self.object.title)
        return super().form_valid(form)

current_date = datetime.datetime.now()


class CourseDetail(FormMixin,DetailView):
    model = Course
    form_class = AttendanceForm
    
    def get_success_url(self):
        return reverse('courses:course_detail', kwargs={'pk': self.object.id})

    def form_valid(self, form: Any):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        object = self.get_object()
        student = self.get_object().students.all()
        payment = self.get_object().payment_set.all()
        attandence = self.object.attendance_set.filter(date=current_date)
        print(student)
        return {
            'object':object,
            'student':student,
            'current_date':current_date,
            'form':AttendanceForm(),
            'attandence':attandence,
            'payment':payment
        }
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        

    def form_valid(self, form):
        form.save()
        return super(CourseDetail, self).form_valid(form)

class PaymentCourseList(ListView):
    model = Course

def payment_view(request,pk):
    template_name = 'courses/course_form.html'
    students = Student.objects.filter(courses=Course.objects.get(id=pk))
   
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            student = form.cleaned_data['user']
            course = form.cleaned_data['course']
            payment_month = student.payment_set.get(date__month=current_date.now().month)
            print(payment_month)
            # payment_month = student.payment_set.annotate(month_stamp=Extract('date', 'month')).values_list('month_stamp', flat=True)
            # payment = student.payment_set.get(date__month=current_date.month)
            if payment_month:
                if payment_month.course == course:
                    return HttpResponse('<h1>This student has already made a payment for this month</h1>')
                else:
                    form.save()
            else:
                form.save()
        else:
            return HttpResponse('<h1>Fill all the fields</h1>')
    else:
        form = PaymentForm()
    context = {
        'form' : form,
        'student' : students
    }
    return render(request, template_name,context)