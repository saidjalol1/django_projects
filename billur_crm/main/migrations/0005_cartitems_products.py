# Generated by Django 4.2.7 on 2023-11-23 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('main', '0004_remove_cartitems_products_cartitems_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='products',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
