# Generated by Django 4.2.7 on 2023-11-25 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_orders_session_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(blank=True, default='active', max_length=250, null=True),
        ),
    ]
