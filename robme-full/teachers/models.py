from django.db import models


class Roles(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)


    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    surname =models.CharField(max_length=200)
    profile_pic  = models.FileField(upload_to='teachers_avatar')
    phone_number = models.CharField(max_length=200)
    salary = models.PositiveBigIntegerField(default=0)
    roles = models.ForeignKey(Roles,on_delete=models.DO_NOTHING, related_name='teachers', blank=True,null=True)


    def salary(self):
        all = sum([(i.price // 100) * 50 for i in self.group.all()])
        return all

    def __str__(self):
        return str(self.name)
    

