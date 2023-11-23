from django.contrib import admin
from .models import ProductCategory, ProductTag


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name', )}


@admin.register(ProductTag)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name', )}
