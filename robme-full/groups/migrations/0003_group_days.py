# Generated by Django 4.2.7 on 2023-11-13 03:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_delete_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='days',
            field=models.CharField(default=datetime.datetime(2023, 11, 13, 3, 32, 44, 989017, tzinfo=datetime.timezone.utc), max_length=200),
            preserve_default=False,
        ),
    ]