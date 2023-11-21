from django import forms
from .models import Course, Student, Teacher, Attendance, Payment



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'courses': forms.SelectMultiple(attrs={'multiple':'','class':'select'})
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'courses': forms.SelectMultiple(attrs={'multiple':'','class':'select'})
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['slug']
        widgets = {
            'title':forms.TextInput(),
            'description':forms.Textarea(),
            'days': forms.SelectMultiple(attrs={'multiple':'','class':'select'})
        }      


class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = '__all__'
        exclude = ['subject']
        widgets = {
            'date': forms.DateInput(
                attrs={'type':'date'})
        }      


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'user' : forms.Select(attrs={'class':'bg-white focus:outline-none border border-gray-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-gray-700'}),
            'course': forms.Select(attrs={'class':'bg-white focus:outline-none border border-gray-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-gray-700'}),
            'date': forms.DateInput(
                attrs={'type':'date','class':'bg-white focus:outline-none border border-gray-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-gray-700'}),
            'active': forms.CheckboxInput()
        }      