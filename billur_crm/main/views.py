from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Orders, OrderItems
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
        if 'delete' in request.POST:
            order_instance = Orders.objects.get(pk=request.POST.get('order'))
            order_instance.delete()
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
    

class OrderDetail(View):
    template_name = 'order_detail.html'

    def get_object(self):
        try:
            object = Orders.objects.get(pk=self.kwargs['pk'])
        except Orders.DoesNotExist:
            raise Http404('Order not found!')
        return object


    def get_context_data(self, **kwargs):
        kwargs['object'] = self.get_object()
        return kwargs
    
    def get(self,request,*args,**kwargs):
        return render(request, self.template_name,self.get_context_data())


    def post(self,request,*args,**kwargs):
        ctxt = {}
        if 'delete' in request.POST:
            print(request.POST.get('product_delete'))
            product_id = request.POST.get('product_delete')
            order_instance = Orders.objects.get(pk=self.get_object().id)
            item = order_instance.order_items.get(id=product_id)
            item.delete()
        return render(request, self.template_name, self.get_context_data(**ctxt))


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


