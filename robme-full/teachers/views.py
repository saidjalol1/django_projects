
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TeacherForm, TeacherUpdateForm, SendSmsForm
from .models import Teacher
from .send_message import send_message

class Teachers(View):
    template_name = 'teachers.html'
    extra_context = {'title':'Teachers'}

    def get_context_data(self, **kwargs):
        kwargs['teachers'] = Teacher.objects.all()
        if 'add_form' not in kwargs:
            kwargs['add_form'] = TeacherForm()
        if 'edit_form' not in kwargs:
            kwargs['edit_form'] = TeacherUpdateForm()
        if 'send_sms_form' not in kwargs:
            kwargs['send_sms_form'] = SendSmsForm()

        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


    def post(self, request, *args, **kwargs):
        ctxt = {}

        if 'edit' in request.POST:
            form = TeacherUpdateForm(request.POST)
            teacher = form.teacher
            if form.is_valid():
                print(teacher.name)
                form.save()
            else:
                ctxt['edit_form'] = form
        elif 'send_sms' in request.POST:
            send_sms_form = SendSmsForm(request.POST)
            if send_sms_form.is_valid():
                message = send_sms_form.cleaned_data['body']
                phone = send_sms_form.cleaned_data['to_who']
                print(phone)
                print(message)
                send_message(phone,message)
            else:
                ctxt['send_sms_form'] = send_sms_form
        elif 'add' in request.POST:
            form = TeacherForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                ctxt['add_form'] = form

        return render(request, self.template_name, self.get_context_data(**ctxt))


class TeacherDetail(View):
    template_name  = 'profile.html'

    def get_object(self):
        try:
            object = Teacher.objects.get(pk=self.kwargs['pk'])
        except Teacher.DoesNotExist:
            raise Http404('Question not found!')
        return object

    def get_context_data(self, **kwargs):
        kwargs['object'] = self.get_object()
        if 'send_sms' not in kwargs:
            kwargs['send_sms'] = SendSmsForm()
        if 'update_form' not in kwargs:
            kwargs['update_form'] = TeacherUpdateForm()

        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        ctxt = {}

        if 'edit' in request.POST:
            teacher = self.get_object()
            form = TeacherUpdateForm(request.POST,instance=teacher)
            if form.is_valid():
                print(teacher.name)
                form.save()
            else:
                ctxt['update_form'] = form
        elif 'send_sms' in request.POST:
            send_sms_form = SendSmsForm(request.POST)
            if send_sms_form.is_valid():
                message = send_sms_form.cleaned_data['body']
                phone = send_sms_form.cleaned_data['to_who']
                print(phone)
                print(message)
                send_message(phone,message)
            else:
                ctxt['send_sms_form'] = send_sms_form

            

        return render(request, self.template_name, self.get_context_data(**ctxt))

