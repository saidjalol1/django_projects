# Generated by Django 4.2.7 on 2023-11-14 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_students_status_students_status_change_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='couse_of_status_change',
            field=models.TextField(blank=True, null=True),
        ),
    ]
