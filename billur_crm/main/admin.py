from django.contrib import admin
from .models import Orders, CartItems, OrderItems, WishList

admin.site.register(Orders)
admin.site.register(CartItems)
admin.site.register(OrderItems)
admin.site.register(WishList)