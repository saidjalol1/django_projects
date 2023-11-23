from django.db import models
from main.models import ProductCategory
from django_resized import ResizedImageField


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)
    image = ResizedImageField(size=[570,650],upload_to='movie_posters/')
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')






