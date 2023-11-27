from django.contrib import admin
from .models import Orders, CartItems, OrderItems

admin.site.register(Orders)
admin.site.register(CartItems)
admin.site.register(OrderItems)