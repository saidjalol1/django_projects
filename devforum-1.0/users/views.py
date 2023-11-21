import requests

from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView
from .models import User
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.conf import settings

def registration(request):
    template_name = 'users/register.html'
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.add_message(request, messages.SUCCESS, f"Welcome { user.username } !!!")
            login(request,user)
            return redirect(f"/users/profile/{ user.id }/")
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
    
    return render(request, template_name, {'form':form})


class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'
