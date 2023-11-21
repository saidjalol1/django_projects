from django import forms
from .models import Students, Payment


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        exclude = ['balance','status','status_change_date','couse_of_status_change','economical_status']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control my-1'}),
            'surname': forms.TextInput(attrs={'class':'form-control my-1'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control my-1','placeholder':'Phone number'}),
            'group': forms.SelectMultiple(attrs={'class':'form-control my-1',}),
        }


class StudentIcedForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        exclude = ['name', 'surname', 'phone_number','balance','economical_status','group']
        widgets = {
            'status':forms.CheckboxInput(),
            'couse_of_status_change': forms.TextInput(attrs={'class':'form-control my-1','placeholder':'deactivatation cause'}),
            'status_change_date': forms.DateInput(attrs={'class':'form-control','type':'date'}),
        }

class StudentsUpdateForm(forms.ModelForm):
    class Meta:
        model   = Students
        fields = '__all__'
        exclude = ['balance','couse_of_status_change','status_change_date','economical_status']
        widgets = {
            'status':forms.CheckboxInput(),
            'name': forms.TextInput(attrs={'class':'form-control my-1'}),
            'surname': forms.TextInput(attrs={'class':'form-control my-1'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control my-1','placeholder':'Phone number'}),
            'group': forms.SelectMultiple(attrs={'class':'form-control my-1',}),
        }

class AddToGroupForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        exclude = ['name', 'surname', 'phone_number','balance','status','status_change_date','couse_of_status_change','economical_status']
        widgets = {
            'group': forms.SelectMultiple(attrs={'class':'form-control my-1',}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__' 
        exclude = ['note','staff']
        widgets = {
            'amount': forms.TextInput(attrs={'class':'form-control my-1'}),
            'student': forms.Select(attrs={'class':'form-control my-1',}),
            'date_added': forms.DateInput(attrs={'class':'form-control my-1','type':'date'}),
            'course': forms.Select(attrs={'class':'form-control my-1',}),
        }