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


# class EventForm(ModelForm):
#   class Meta:
#     model = Event
#     # datetime-local is a HTML5 input type, format to make date time show on fields
#     widgets = {
#         'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
#         'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
#     }
#     fields = '__all__'

#   def __init__(self, *args, **kwargs):
#     super(EventForm, self).__init__(*args, **kwargs)
#     # input_formats parses HTML5 datetime-local input to datetime field
#     self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
#     self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
