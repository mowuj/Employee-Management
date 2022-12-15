from .models import *
from django.forms import ModelForm, DateInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class EmployeeAddForm(ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
        # exclude=("username",)


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['email','employee_id']
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

class LeaveForm(ModelForm):
    class Meta:
        model=Leave
        fields=[
            'cause_of_leave',
            'start_date',
            'end_date'
        ]
        widgets = {
            'cause_of_leave': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2','placeholder': 'Cause of Leave'}),
            'start_date': forms.DateInput(format=('%d/%m/%y'), attrs={'class': 'form-control bg-light badge-pill p-2', 'type': 'date'}),
            'end_date': forms.DateInput(format=(' % d/%m/%y'), attrs={'class ': 'form-control bg-light badge-pill p-2', 'type': 'date'}),

        }

class MeetingForm(ModelForm):
    class Meta:
        model=Meeting
        fields=[
            'name',
            'person_with',
            'meeting_date',
            'meeting_time',
            
        ]
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2', 'placeholder': 'Name...'}),
            'person_with': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2', 'placeholder': 'Meeting With...'}),
            'meeting_date': forms.DateInput(format=(' % d/%m/%y'), attrs={'class ': 'form-control bg-light badge-pill p-2', 'type': 'date'}),
            'meeting_time': forms.TimeInput(format=('%H:%M'), attrs={'type': 'time',
                'class': 'form-control bg-light badge-pill'})
        }

class ClientForm(ModelForm):
    class Meta:
        model=Client
        fields='__all__'