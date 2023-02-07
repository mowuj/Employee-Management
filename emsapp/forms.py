from .models import *
from django.forms import ModelForm, DateInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control bg-light badge-pill p-2 m-2','type':'password', 'name': 'password','placeholder':'Enter Password'}),
    label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control bg-light badge-pill p-2 m-2','type':'password', 'name': 'password','placeholder':'Confirm Password'}),
    label='Password')
    class Meta:
        model = User
        fields = ['username','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'UserName..','label':'Department Name'}),
                                            
        }

class EmployeeAddForm(ModelForm):
    class Meta:
        model=Employee
        fields=[
            'name',
            'email',
            'phone',
            'nid',
            'ssc',
            'hsc',
            'honors',
            'masters',
            'salary',
            'father_name',
            'mother_name',
            'district',
            'image',
            
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Your Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Your Phone'}), 
            'nid': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Nid no'}), 
            'ssc': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter SSC Result'}),
            'hsc': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter HSC Result'}),
            'honors': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Honors Result'}),
            'masters': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Masters Result'}),
            'salary': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Salary'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Your Father Name'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Your Mother Name'}),
            'district': forms.Select(attrs={'class': 'form-control bg-light badge-pill p-2',
                                            'placeholder': 'Enter Your District'}),
            # 'image': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2',
            #                                 'placeholder': 'Enter Your Image'}),
            "image":forms.ClearableFileInput(attrs={"class":"form-control bg-light badge-pill p-2 m-2"}),
        }
       

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = [
                'name',
                'email',
                'employee_id',
                'salary',
                'phone',
                'post',
                'department']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Full Name..','label':'User Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Email..','label':'Email'}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Employee ID..','label':'Employee ID'}),
            'salary': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Employee Salary..','label':'Employee Salary'}),
            'phone': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Employee Phone..','label':'Employee Salary'}),
            'post': forms.Select(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Post'}),
            'department': forms.Select(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Department'}),
                                            
        }

class DepartmentAddForm(ModelForm):
    class Meta:
        model=Department
        fields=[
            'name',
            'manager',
            'start_date',
            'image'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2',
                                            'placeholder': 'Enter Department Name..','label':'Department Name'}),
            'manager': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2',
                                            'placeholder': 'Enter Manager Name..','label':'Manager Name'}),
            'start_date': forms.DateInput(format=('%d/%m/%y'), attrs={'class': 'form-control bg-light badge-pill p-2', 'type': 'date'}),
            "image":forms.ClearableFileInput(attrs={"class":"form-control bg-light badge-pill p-2 m-2"})
        }

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
        fields=[
            'client_name',
            'client_id',
            'email',
            'phone',
            'company_name'
        ]
        widgets={
            'client_name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'placeholder': 'Client Name...'}),
            'client_id': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'placeholder': 'Client Id...'}),
            'email': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'placeholder': 'Client email...'}),
            'phone': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'placeholder': 'Client Phone...'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'placeholder': 'Company Name...'}),
        }