import math
from datetime import datetime, timedelta, date
from django.db import models
from teachers.models import Teacher




class Room(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveBigIntegerField(default=0)
    time = models.CharField(max_length=200)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, related_name='groups')
    days = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, related_name='group')
    started_date = models.DateField()
    ends_in = models.DateField()

    def remainded_time(self):
        now = date.today()
        started_date = self.started_date
        ends_in = self.ends_in

        if now > ends_in or now == ends_in:
            return "Event has already ended."
        else:
            interval = ends_in - now
            average_days_per_month = 30.44
            total_days = interval.days
            months = total_days / average_days_per_month
            return f"Month left: {math.floor(months)}"

    def __str__(self):
        return str(self.name) + " " + str(self.time) + " " + str(self.days)
    

# class DeactivateStudent(models.Model):
#     student = models.ForeignKey(Students, on_delete=models.DO_NOTHING, related_name='deactivated')
#     group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='deactivated_students')