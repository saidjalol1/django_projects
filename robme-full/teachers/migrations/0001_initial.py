# Generated by Django 4.2.7 on 2023-11-11 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('profile_pic', models.FileField(upload_to='teachers_avatar')),
                ('phone_number', models.CharField(max_length=200)),
                ('salary', models.PositiveBigIntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, related_name='teachers', to='groups.groups')),
                ('roles', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='teachers', to='teachers.roles')),
            ],
        ),
    ]
