from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views import View

from .models import Orders



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


class Storage(TemplateView):
    template_name = 'ombor.html'

# class Customers(TemplateView):
#     template_name = 'customers/ecom-customers.html'


# class CustomersProfile(TemplateView):
#     template_name = 'customers/customers_profile.html'


# class CardPage(TemplateView):
#     template_name = 'card_page.html'


# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)

#     cart_item, created = CartItem.objects.get_or_create(
#         product=product,
#         user=request.user if request.user.is_authenticated else None
#     )

#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()

#     # Store cart in session
#     if 'cart' not in request.session:
#         request.session['cart'] = []

#     request.session['cart'].append({
#         'product_id': product_id,
#         'quantity': cart_item.quantity,
#     })

#     return HttpResponse("Product added to cart.")