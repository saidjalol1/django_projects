from django import forms
from .models import Group
from students.models import Payment

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        # exclude = ['groups','profile_pic','salary','roles']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control my-1','placeholder':'Name'}),
            'price' : forms.TextInput(attrs={'class':'form-control my-1','placeholder':'price'}),
            'time' : forms.TextInput(attrs={'class':'form-control my-1','placeholder':'time'}),
            'days' : forms.TextInput(attrs={'class':'form-control my-1','placeholder':'days'}),
            'room' : forms.Select(attrs={'class':'form-control my-1'}),
            'teacher' : forms.Select(attrs={'class':'form-control my-1'}),
            'started_date': forms.DateInput(
                attrs={'type':'date','class':'form-control my-1'}),
            'ends_in' : forms.DateInput( attrs={'type':'date','class':'form-control my-1'}),
        }


class GroupUpdateForm(forms.ModelForm):
    class Meta:
        model = Group   
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control my-1','placeholder':'Name'}),
            'price' : forms.TextInput(attrs={'class':'form-control my-1','placeholder':'price'}),
            'time' : forms.TextInput(attrs={'class':'form-control my-1','placeholder':'time'}),
            'days' : forms.TextInput(attrs={'class':'form-control my-1','placeholder':'days'}),
            'room' : forms.Select(attrs={'class':'form-control my-1'}),
            'teacher' : forms.Select(attrs={'class':'form-control my-1'}),
            'started_date': forms.DateInput(
                attrs={'type':'date','class':'form-control my-1'}),
            'ends_in' : forms.DateInput( attrs={'type':'date','class':'form-control my-1'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        exclude = ['note']
        widgets = {
            'date_added' : forms.DateInput(attrs={'class':'form-control my-1','type':'date'}),
            'amount' : forms.TextInput(attrs={'class':'form-control my-1','placeholder':'amount'}),
            'student' : forms.Select(attrs={'class':'form-select my-1'}),
            'course' : forms.Select(attrs={'class':'form-select my-1'}),
        }
# class GroupUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Group
#         fields = '__all__'
#         widgets = {
#             'name' : forms.TextInput(attrs={'class':'form-control my-1','placeholder':'Name'}),
#             'surname' : forms.TextInput(attrs={'class':'form-control my-1','placeholder':'Name'}),
#             'phone_number' : forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Phone number','type':'tel'}),
#         }