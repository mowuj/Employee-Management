from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password',]
class EmployeeAddForm(ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
        # exclude=("username",)

class TaskForm(ModelForm):
    class Meta:
        model=DailyTask
        fields=[
            'title',
            'description',
            'delivery'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2',
                                            'placeholder': 'Enter Your Task Title'}),

            'description': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2',
                                                  'placeholder': 'Enter Your Task Description '}),
            'delivery': forms.DateInput(format=('%d/%m/%y'), attrs={'class': 'form-control bg-light badge-pill p-2', 'type': 'date'}),

        }
