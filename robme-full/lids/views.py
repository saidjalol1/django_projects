from typing import Any
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views import View
from django.views.generic.edit import DeleteView, UpdateView, CreateView , FormMixin, FormView
from .models import Lids, LidObjects
from .forms import LidObjectsForm


class Lid(CreateView):
    model = LidObjects
    template_name = 'lidlar.html'
    form_class = LidObjectsForm
    success_url = reverse_lazy('lids:lids_render')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'lids' : Lids.objects.all(),
            'to_center' : Lids.objects.get(name ='Markazga').lid_objects.all(),
            'came_to_center' : Lids.objects.get(name ='Markazga kelganlar').lid_objects.all(),
            'telegram' : Lids.objects.get(name = 'Telegram').lid_objects.all(),
            'friend' : Lids.objects.get(name = 'Friend').lid_objects.all(),
            'walked_by' : Lids.objects.get(name = 'Walked by').lid_objects.all(),
            'form': LidObjectsForm(),
            'count' : LidObjects.objects.count(),
        }
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)