# Generated by Django 4.2.7 on 2023-11-13 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_delete_groups'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='group',
            field=models.ManyToManyField(blank=True, related_name='students', to='groups.group'),
        ),
    ]