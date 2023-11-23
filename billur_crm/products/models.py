from django.db import models
from main.models import ProductCategory, ProductTag
from django_resized import ResizedImageField


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    image = ResizedImageField(size=[570,650],upload_to='movie_posters/')
    description = models.TextField(blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    tag = models.ForeignKey(ProductTag, on_delete=models.CASCADE, related_name='products', blank=True, null=True)


    def __str__(self):
        return str(self.name)
    



