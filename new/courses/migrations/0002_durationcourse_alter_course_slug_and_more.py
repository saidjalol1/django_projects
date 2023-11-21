# Generated by Django 4.2.7 on 2023-11-06 14:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DurationCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_start_date', models.DateTimeField(default=0)),
                ('course_end_date', models.DateTimeField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='course_start_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.durationcourse'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_start_year',
            field=models.ForeignKey(blank=True, default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='courses.durationcourse'),
            preserve_default=False,
        ),
    ]
