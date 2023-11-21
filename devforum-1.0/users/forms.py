from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField
from .models import User


class RegisterForm(UserCreationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)