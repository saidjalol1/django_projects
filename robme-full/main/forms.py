from django import forms

class UnpaidPaymentsFilterForm(forms.Form):
    month = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))