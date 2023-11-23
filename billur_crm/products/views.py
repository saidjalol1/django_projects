from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Product,ProductCategory, ProductTag

class ProductsList(ListView):
    model = Product
    template_name = 'products/ecom-product-grid.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'products': Product.objects.all(),
            'categories': ProductCategory.objects.all(),
            'tag': ProductTag.objects.all(),
        }
        # print(context['products'])
        return context


    def get(self,request,*args,**kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)
        if 'billur_products' in  request.GET:
            context['products'] = Product.objects.filter(category__name='Billur tovarlari')
        elif 'extra-products' in request.GET:
            context['products'] = Product.objects.filter(category__name='Boshqalar')
        else:
            context['products'] = context
        return render(request,self.template_name,context)



class ProductDetail(TemplateView):
    template_name = 'products/ecom-product-detail.html'