from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)


    def __str__(self):
        return str(self.name)
    


