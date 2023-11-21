from django import forms
from .models import Teacher
from main.models import TextMessage
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['groups','profile_pic','salary','roles']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control my-1','placeholder':'Name'}),
            'surname' : forms.TextInput(attrs={'class':'form-control my-1','placeholder':'Name'}),
            'phone_number' : forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Phone number','type':'tel'}),
        }

class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['salary','roles']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control my-1','placeholder':'Name'}),
            'surname' : forms.TextInput(attrs={'class':'form-control my-1','placeholder':'Name'}),
            'phone_number' : forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Phone number','type':'tel'}),
            'profile_pic' : forms.FileInput(attrs={'class':'form-control my-1'})
        }


class SendSmsForm(forms.ModelForm):
    class Meta:
        model = TextMessage
        fields = '__all__'
        exclude = ['from_who']
        widgets = {
            'to_who' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.TextInput(attrs={'class':'form-control my-1'}),
        }