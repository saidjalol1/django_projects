# Generated by Django 4.2.7 on 2023-11-14 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_alter_group_teacher'),
        ('students', '0004_alter_payment_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='students',
            name='status_change_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Attandence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='attandence', to='groups.group')),
                ('student', models.ManyToManyField(related_name='attandence', to='students.students')),
            ],
        ),
    ]
