from django import forms
from .models import Problem, Solve


class Problem_Form(forms.ModelForm):

    class Meta:
        model = Solve
        fields = ['body','tags']