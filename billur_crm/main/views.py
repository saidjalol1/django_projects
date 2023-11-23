from django.shortcuts import render
from django.views.generic import TemplateView


class StatisticsView(TemplateView):
    template_name = 'index.html'


class Customers(TemplateView):
    template_name = 'customers/ecom-customers.html'


class CustomersProfile(TemplateView):
    template_name = 'customers/customers_profile.html'


class CardPage(TemplateView):
    template_name = 'card_page.html'