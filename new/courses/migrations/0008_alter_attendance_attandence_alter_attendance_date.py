# Generated by Django 4.2.7 on 2023-11-07 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_attendance_attandence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attandence',
            field=models.CharField(choices=[('true', 'Keldi'), ('false', 'Kelmadi')], max_length=40),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
