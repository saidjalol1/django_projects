from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Problem, Solve
from django.template.defaultfilters import slugify



class HomePage(ListView):
    model = Problem
    template_name = 'index.html'

class ProblemDetail(DetailView):
    model = Problem
    template_name = 'forum/problem_detail.html'

class AddProblem(LoginRequiredMixin,CreateView):
    login_url = '/users/login'
    template_name = 'forum/problem_add.html'

    model = Problem
    fields = ['title', 'tags', 'body']
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = slugify(self.object.title)
        self.object.author = self.request.user
        return super().form_valid(form)