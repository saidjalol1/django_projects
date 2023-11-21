# Generated by Django 4.2.7 on 2023-11-08 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_alter_attendance_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendence_student', to='courses.student', unique_for_date=True),
        ),
    ]