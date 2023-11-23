from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductsList.as_view(), name='product_list'),
    path('products/products_id', views.ProductDetail.as_view(), name='product_detail'),
]