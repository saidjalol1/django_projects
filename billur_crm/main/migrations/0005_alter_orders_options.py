# Generated by Django 4.2.7 on 2023-11-29 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_wishlist_quantity_remove_wishlist_products_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'ordering': ['-date_added']},
        ),
    ]
