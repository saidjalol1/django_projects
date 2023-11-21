from django import forms
from .models import LidObjects


class LidObjectsForm(forms.ModelForm):
    class Meta:
        model = LidObjects
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control shadow-none my-1 border-0', 'type':"text",'placeholder':'Ism','autofocus':'true', 'required':'true'}),
            'surname' : forms.TextInput(attrs={'class':'form-control shadow-none my-1 border-0', 'type':"text",'placeholder':'Familiya','autofocus':'true', 'required':'true'}),
            'lid' : forms.Select(attrs={'class':'form-select shadow-none border-0','style':'cursor: pointer;'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control shadow-none my-1 border-0','type':"tel",'placeholder':"Telefon",'required':'true'}),
            'comment':forms.TextInput(attrs={'class':'form-control shadow-none my-1 border-0','placeholder':"Comment"}),
        }