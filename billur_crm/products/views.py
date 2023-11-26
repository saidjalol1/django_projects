import copy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Product, ProductCategory, ProductTag
from django.http import HttpResponse
from main.models import Orders, CartItems
from django.views import View
from main.models import Orders
from .forms import ProductAddForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin

class ProductsList(FormMixin,ListView):
    model = Product
    form_class = ProductAddForm
    template_name = 'products/ecom-product-grid.html'
    paginate_by = 8
    success_url = reverse_lazy('/')

    
    def get_queryset(self):
        queryset = super().get_queryset()
        if 'billur_products' in self.request.GET:
            queryset = queryset.filter(category__name='Billur')
        elif 'extra-products' in self.request.GET:
            queryset = queryset.filter(category__name='Boshqalar')
        elif 'search' in self.request.GET:
            queryset = queryset.filter(name__icontains=self.request.GET.get('product'))
        return queryset



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'categories': ProductCategory.objects.all(),
            'tags': ProductTag.objects.all(),
            'form': ProductAddForm()
        })
        return context

   
    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle form submission for invalid data
        return self.render_to_response(self.get_context_data(form=form, object_list=self.get_queryset()))


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/ecom-product-detail.html'


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    session_key = request.session.session_key
    quantity = request.POST.get('quantity')
    

    if not session_key:
        request.session.save()
        session_key = request.session.session_key

    
    try:
        cart_item = CartItems.objects.get(session_key=session_key, product_id=product.id)
        if product.amount == 0 or product.amount < int(quantity):
            return HttpResponse('<h1>Omborda Mahsulot yetrali emas</h1>')

        cart_item.quantity += int(quantity)
        cart_item.save()


    except CartItems.DoesNotExist:
        quantity = int(quantity)
        CartItems.objects.create(
            product_id=product_id,
            session_key=session_key,
        )
        cart_item = CartItems.objects.get(session_key=session_key, product_id = product_id)
        cart_item.quantity += quantity
        cart_item.save()

    return redirect('products:product_list')



class CardView(View):
    template_name ='card_page.html'

    def get_context_data(self, request,**kwargs):
        session_key = request.session.session_key
        try:
            cart_items = CartItems.objects.filter(session_key=session_key)
        except CartItems.DoesNotExist:
            return HttpResponse('<h1>Savatcha Mahsuotlari topilmadi!!! oldin Savatchaga mahsulot qo\'shing</h1>')
        kwargs['cart_items'] = cart_items
        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(request))


    def post(self, request, *args, **kwargs):
        ctxt = {}

        if 'add_quantity' in request.POST:
            product = CartItems.objects.get(product_id=request.POST.get('product'))
            quantity = request.POST.get('quantity')
            calculate = product.quantity + int(quantity)
            print(calculate)
            if product.product.amount < (product.quantity + int(quantity)):
                return HttpResponse(f"<h1>Bu mahsulot omborda {product.product.amount }ta qolgan holos !!!</h1>")
            else:
                product.quantity = int(quantity)
                product.save()

        elif 'delete' in request.POST:
            product = CartItems.objects.get(product_id=request.POST.get('product_delete'))
            base_product = Product.objects.get(id=product.product.id)
            base_product.amount += product.quantity
            base_product.save()
            product.delete()
        elif 'order' in request.POST:
            session_key = request.session.session_key
            cart_items = CartItems.objects.filter(session_key=session_key)
            order_amount = sum([i.overall_price() for i in cart_items])
    
            if order_amount > 100000:
                order_instance = Orders.objects.create(
                customer_full_name=request.POST.get('customer_full_name'),
                address=request.POST.get('address'),
                target=request.POST.get('target'),
                phone_number=request.POST.get('phone_number'),
                session_key=session_key,
                )
        
                order_instance.items.set(cart_items)
        else:
            print(sum([i.overall_price() for i in cart_items]))
            return HttpResponse("<h1>Umumiy qiymat 100000 so'mni tashkil etganda buyurtma berish mumkin!!!</h1>")
            



        return render(request, self.template_name, self.get_context_data(request,**ctxt))


class CustomerOrdersView(View):
    template_name = 'customers/customer_orders.html'

    def get_context_data(self, *args, **kwargs):
        return kwargs
    

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        session_key = request.session.session_key
        context['orders'] = Orders.objects.filter(session_key=session_key)
        return render(request, self.template_name, context)
    

    def post(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, self.get_context_data(**context))

class CustomerOrderDetail(DetailView):
    model = Orders
    template_name = 'order_detail.html'