from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.template.defaultfilters import slugify


# class Days(models.TextChoices):
#     monday = "Monday", _("Monday")
#     tuesday = "Tuesday", _("Tuesday")
#     wednesday = "Wednesday", _("Wednesday")
#     thursday = "Thursday ", _("Thursday")
#     friday = "Friday", _("Friday")
#     saturday = "Saturday", _("Saturday")
#     sunday = "Sunday", _("Sunday")

class Days(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)


    def __str__(self):
        return self.name
    

class Course(models.Model):
#     DEMO_CHOICES =( 
#     ("Du", "Dushanba"), 
#     ("se", "Seshanba"), 
#     ("chor", "Chorshanba"), 
#     ("pa", "Payshanba"), 
#     ("ju", "Juma"), 
#     ("shan", "Shanba"), 
#     ("yak", "Yakshanba"), 
# ) 
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    fixed_price = models.PositiveIntegerField(default=0)
    days = models.ManyToManyField(Days)
    time = models.CharField(max_length=40)


    def __str__(self):
        return self.title


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    courses = models.ManyToManyField(Course, related_name='teacher')


    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    courses = models.ManyToManyField(Course, related_name='students')
    
    
    def __str__(self):
        return self.name


class Attendance(models.Model):
    DEMO_CHOICES =( 
    ("true", "Keldi"), 
    ("false", "Kelmadi"),
    ) 
    user = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='attendence_student',unique_for_date='date')
    subject = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField()
    attandence = models.CharField(max_length=40,choices=DEMO_CHOICES)

    def __str__(self):
        return f"{self.user.name} - {self.date}"

class Payment(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    date = models.DateTimeField()
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.user.name
    

# Signals
# @receiver(post_save, sender=Problem)
# def attendence_created(sender,instance, created,  **kwargs):
#     if created:
#         student = instance
#         print(student.courses.all())
#         problem = Attendance.objects.create(
#             user = student,
#             # subject = student.courses,
#             date =  datetime.now(),
#             attandence = 'true'
#         )
# @receiver(post_delete, sender=Problem)
# def probleme_deleted(sender, instance,**kwargs):
#     print('Post deleted')
#     print('Post was', instance.title)

# post_save.connect(attendence_created,sender=Student)
# post_delete.connect(probleme_deleted,sender=Problem)