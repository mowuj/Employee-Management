from django.shortcuts import render,redirect
from .models import *
# from django.contrib.auth.decorators import login_require
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import *
from .filters import *
from django.db.models import Sum,Q
import datetime
from datetime import date


# Create your views here.
def home(request):
    return render(request,'home.html')

def create_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password = request.POST['password']
        con_password = request.POST['con_password']
        try:
            user=User.objects.get(username=username)
            if user:
                msg="This username already taken"
                context={'msg':msg}
                return render(request,'signup.html',context)

        except:
            if password==con_password:
                user=User.objects.create_user(username=username,password=password)
                # employee=Employee.objects.create()
                if user:
                    return redirect('/')
        else:
            msg='Password does not matched'
            context={'msg':msg}
            return redirect(request,'signup.html',context)
    return render(request,'signup.html')
def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('/home')
        else:
            msg="Username or password is Incorrect"
            context={'msg':msg}
            return render(request,'login.html',context)
    return render (request,'login.html')

def add_employee(request):
    form=EmployeeAddForm()
    if request.method=='POST':
        form=EmployeeAddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            context={'form':form}
            return redirect('add_employee.html')
    form=EmployeeAddForm()
    context={'form':form}
    return render(request,'add_employee.html',context)

def all_employee(request):
    all_employee = Employee.objects.all()
    myfilter=EmployeeFilter(request.GET,queryset=all_employee)
    all_employee=myfilter.qs
    context = {'all_employee': all_employee, 'myfilter': myfilter}
    return render(request,'all-employee.html',context)

def employee_detail(request,id):
    detail=Employee.objects.filter(id=id)
    context={'detail':detail}
    return render(request,'detail.html',context)

def profile(request):
    user=request.user
    profile=Employee.objects.get(username=user)
    department=profile.department
    dept=Employee.objects.filter(department=department)
    context={'profile':profile,'dept':dept}
    return render(request,'profile.html',context)


def profile_detail(request,id):
    details = Employee.objects.filter(id=id)
    context = {'details': details}
    return render(request, 'profile-detail.html', context)

def edit_profile(request,id):
    employee=Employee.objects.get(id=id)
    form = EmployeeAddForm(instance=employee)
    if request.method =='POST':
        form = EmployeeAddForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()  
            return redirect('/profile')
    context = {'form':form}
    return render (request,'edit-profile.html',context)
def delete(request):
    remove=Employee.objects.get(id=id)
    remove=remove.delete()
    return('/all-employee')