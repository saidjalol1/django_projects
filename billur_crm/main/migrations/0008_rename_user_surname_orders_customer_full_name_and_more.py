# Generated by Django 4.2.7 on 2023-11-24 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_cartitems_order_orders_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='user_surname',
            new_name='customer_full_name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='username',
        ),
    ]