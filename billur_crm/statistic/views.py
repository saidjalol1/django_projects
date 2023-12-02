from django.shortcuts import render, redirect
from django.db.models import Sum, F
from django.db.models.functions import TruncMonth
from django.views import View
from django.shortcuts import render
from products.models import Product
from main.models import OrderItems, Orders, Expenses
from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.db.models import Count
from .forms import ExpensesForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StatisticsView(View):
    template_name = 'index.html'


    def get_context_data(self,*args,**kwargs):
        try:
            data = Orders.objects.filter(status='Jonatildi').annotate(
                 month=TruncMonth('date_added')
                        ).values('month').annotate(
                                    total_quantity=Sum(F('order_items__products__price') * F('order_items__quantity')),
                                        order_count=Count('id')
                                                ).order_by('month')
            data_list = [
            {'month': entry['month'].strftime('%Y-%m-%d'), 'total_quantity': entry['total_quantity']}
            for entry in data
            ]
        except Orders.DoesNotExist:
            print('error')

        try:
            expenses = Expenses.objects.annotate(
                                month=TruncMonth('date_added')
                                            ).values('month').annotate(
                                                    total_amount=Sum('amount')
                                                            ).order_by('month')
            expenses_list = [
                {'month': entry['month'].strftime('%Y-%m-%d'), 'total_amount': entry['total_amount']}
                for entry in expenses
            ]
        except Expenses.DoesNotExist:
            print('doesnt exite')
        try:
            per_worker = Orders.objects.filter(status='Jonatildi').annotate(
                 month=TruncMonth('date_added')
                        ).values('month', 'received_admin').annotate(
                                    total_quantity=Sum(F('order_items__products__price') * F('order_items__quantity')),
                                        order_count=Count('id')
                                                ).order_by('month')
            per_worker_list = [
            {'month': entry['month'].strftime('%Y-%m-%d'), 'seller': entry['received_admin'], 'total_quantity': entry['total_quantity']}
            for entry in per_worker
            ]
        except Orders.DoesNotExist:
            print('error')

        data_json = json.dumps(data_list, cls=DjangoJSONEncoder)
        expenses_json = json.dumps(expenses_list, cls=DjangoJSONEncoder)
        per_worker_lists_json = json.dumps(per_worker_list, cls=DjangoJSONEncoder)
        kwargs['data'] = data_json
        kwargs['expenses'] = expenses_json
        kwargs['workers'] = per_worker_lists_json
        kwargs['expensesForm'] = ExpensesForm()
        kwargs['sellerForm'] = UserCreationForm()
        kwargs['users'] = User.objects.filter()
        return kwargs


    def get(self,request,*args,**kwargs):
        return render(request,self.template_name, self.get_context_data())
    

    def post(self,request,*args,**kwargs):
        ctxt = {}
        if 'add_expense' in request.POST:
            form = ExpensesForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)
                return render('/')
        if 'add_seller' in request.POST:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                seller =  form.save(commit=False)
                print(seller)
                seller.is_staff = True
                print(dir(seller))
                seller.save()
            else:
                return redirect('/')
        return render(request,self.template_name,self.get_context_data(**ctxt))