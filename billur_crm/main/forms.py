from django import forms
from .models import Orders, Deliver


class DriverForm(forms.ModelForm):
    class Meta:
        model = Deliver
        fields = '__all__'