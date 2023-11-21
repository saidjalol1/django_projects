
from django.db import models
from groups.models import Group
from main.models import Staff


# class IcedStudents(models.Model):
#     date_added = models.DateTimeField(auto_now_add=True)
#     cause = models.TextField()




class Students(models.Model):
    name  =  models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    balance = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=200)
    added_time = models.DateField(auto_now_add=True)
    group = models.ManyToManyField(Group, related_name='students', blank=True)
    status = models.BooleanField(default=True)
    couse_of_status_change = models.TextField(blank=True, null=True)
    status_change_date = models.DateTimeField(blank=True, null=True)
    economical_status = models.BooleanField(default=False)


    def student_payment(self):
        price = []
        for i in self.group.all():
            price.append(i.price)
        return sum(price)
    

    

    def get_fullname(self):
        return str(self.name) + " " + str(self.surname)
    # def student_balance(self):
    #     balance = self.balance 
    #     if 
    #     return balance

    def __str__(self):
        return self.name


class Payment(models.Model):
    date_added = models.DateField()
    amount = models.PositiveIntegerField(default=0)
    note = models.CharField(max_length=200,blank=True, null=True)
    student = models.ForeignKey(Students, on_delete=models.DO_NOTHING, related_name='payments')
    course = models.ForeignKey(Group,on_delete=models.CASCADE, related_name='payments')
    # status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_added']


    def __str__(self):
        return self.course.name


class Attandence(models.Model):
    student = models.ForeignKey(Students,related_name='attandence', on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, related_name='attandence')
    date_added = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date_added) + " attandence for " + str(self.group)
