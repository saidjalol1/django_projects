# Generated by Django 4.2.7 on 2023-11-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_cartitems_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='products',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
