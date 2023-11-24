from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductsList.as_view(), name='product_list'),
    path('products/<pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('product/add_to_card/<product_id>', views.add_to_cart, name='add_to_card'),
    path('cart_page/', views.CardView.as_view(), name='cart'),
]