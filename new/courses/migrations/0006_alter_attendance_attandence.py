# Generated by Django 4.2.7 on 2023-11-07 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_attendance_attandence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attandence',
            field=models.BooleanField(default=False),
        ),
    ]
