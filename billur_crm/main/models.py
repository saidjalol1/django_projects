from django.db import models
from products.models import Product
from django.contrib.auth.models import User


    


    

class CartItems(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    session_key = models.CharField(max_length=40, null=True, blank=True)


    def overall_price(self):
        if self.product.discount != 0:
            return self.product.price - ((self.product.price / 100) * self.product.discount)
        else:
            return int(self.product.price * self.quantity)
        
    



class Orders(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    customer_full_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    target = models.CharField(max_length=250)
    direction = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    status = models.CharField(max_length=250,null=True,blank=True,default='active')
    # products = models.ManyToManyField(Product, related_name='order')
    # discount = models.PositiveBigIntegerField(default=0)

    def get_overall(self):
        return 0


class OrderItems(models.Model):
    quantity = models.PositiveBigIntegerField(default=0)
    products = models.ForeignKey(Product,on_delete=models.CASCADE, blank=True, null=True)
    sessionkey = models.CharField(max_length=40, blank=True, null=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name = 'order_items',blank=True, null=True)


    def __str__(self):
        return str(self.order.customer_full_name)