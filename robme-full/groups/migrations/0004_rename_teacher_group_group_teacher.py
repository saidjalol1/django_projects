# Generated by Django 4.2.7 on 2023-11-13 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_group_days'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='teacher_group',
            new_name='teacher',
        ),
    ]
