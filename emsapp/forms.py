from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class EmployeeAddForm(ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
        exclude=("username",)