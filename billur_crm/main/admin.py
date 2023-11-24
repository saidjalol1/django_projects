from django.contrib import admin
from .models import Orders, CartItems

admin.site.register(Orders)
admin.site.register(CartItems)