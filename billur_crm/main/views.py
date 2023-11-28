from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Orders
from products.models import Storage




class StatisticsView(TemplateView):
    template_name = 'index.html'


class OrdersView(View):
    template_name = 'products/ecom-product-order.html'


    def get_context_data(self, *args, **kwargs):
        kwargs['orders'] = Orders.objects.all()
        return kwargs
    

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    

    def post(self, request, *args, **kwargs):
        context = {}
        if 'ready' in request.POST:
            order = Orders.objects.get(id=request.POST.get('order'))
            order.status = request.POST.get('ready')
            order.save()
        if 'send' in request.POST:
            order = Orders.objects.get(id=request.POST.get('order'))
            order.status = request.POST.get('send')
            order.save()
        if 'is_being' in request.POST:
            order = Orders.objects.get(id=request.POST.get('order'))
            order.status = request.POST.get('is_being')
            order.save()
        if 'received' in request.POST:
            order = Orders.objects.get(id=request.POST.get('order'))
            order.status = request.POST.get('received')
            order.save()
        if 'cancel' in request.POST:
            order = Orders.objects.get(id=request.POST.get('order'))
            order.status = request.POST.get('cancel')
            order.save()
        return render(request, self.template_name, self.get_context_data(**context))



class OrdersStatusView(View):
    template_name = 'products/ecom-product-order.html'

    def get_context_data(self,*args,**kwargs):
        kwargs['orders'] = Orders.objects.all()
        return kwargs

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())
    

    def post(self,request,*args,**kwargs):
        context = {}
        return render(request,self.template_name, self.get_context_data(**context))
    

class OrderDetail(DetailView):
    model = Orders
    template_name = 'order_detail.html'


class StorageView(View):
    template_name = 'ombor.html'


    def get_context_data(self,**kwargs):
        kwargs['products'] = Storage.objects.get(id=1)
        print(kwargs['products'].overall_products_number())
        return kwargs
    

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,self.get_context_data())


    def post(self, request,*args,**kwargs):
        ctxt = {}
        return render(request, self.template_name, self.get_context_data(**ctxt))


