from django.contrib import admin
from .models import *


@admin.register(Days)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    list_filter = ['name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    list_filter = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    prepopulated_fields = {'slug':('title',)}



admin.site.register(Payment)
admin.site.register(Attendance)
