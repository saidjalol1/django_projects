# Generated by Django 4.2.7 on 2023-11-13 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_remove_teacher_groups'),
        ('groups', '0004_rename_teacher_group_group_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='group', to='teachers.teacher'),
        ),
    ]
