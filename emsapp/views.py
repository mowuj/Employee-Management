from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# from django.contrib.auth.decorators import login_require
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .filters import *
from django.db.models import Sum, Q
import datetime
from datetime import date

import holidays

def home(request):
    return render(request, 'home.html')

def create_user(request):
    if request.method == 'POST':
        fm = SignUpForm(data=request.POST)
        form = EmployeeForm(data=request.POST)
        if fm.is_valid() and form.is_valid():
           user = fm.save()
           user.set_password(user.password)

           user_form = form.save(commit=False)
           user_form.user = user
           
           user_form.save()
           messages.success(request, 'Account Created !')
    else:
        fm = SignUpForm()
        form = EmployeeForm()

    context = {'fm': fm, 'form': form}
    return render(request, 'signup.html', context)

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid Username or Password')
        else:
            messages.error(request, 'Invalid Username or Password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def add_employee(request):
    form = EmployeeAddForm()
    if request.method == 'POST':
        form = EmployeeAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {'form': form}
            return redirect('all-employee')
    form = EmployeeAddForm()
    context = {'form': form}
    return render(request, 'add_employee.html', context)


def all_employee(request):
    all_employee = Employee.objects.all()
    myfilter = EmployeeFilter(request.GET, queryset=all_employee)
    all_employee = myfilter.qs
    context = {'all_employee': all_employee, 'myfilter': myfilter}
    return render(request, 'all-employee.html', context)


def employee_detail(request, id):
    detail = Employee.objects.filter(id=id)
    context = {'detail': detail}
    return render(request, 'detail.html', context)


def profile(request):
    profile = Employee.objects.get(user=request.user)
    # department = profile.department
    # dept = Employee.objects.filter(department=department)
    context = {'profile': profile, }
    return render(request, 'profile.html', context)


def profile_detail(request, id):
    details = Employee.objects.filter(id=id)
    context = {'details': details}
    return render(request, 'profile-detail.html', context)


def edit_profile(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeAddForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeAddForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    context = {'form': form}
    return render(request, 'edit-profile.html', context)



def delete(request, id):
    remove = Employee.objects.filter(id=id)
    remove = remove.delete()
    return redirect('/all-employee')

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.do_status = True
            form = form.save()
            msg = " Submitted "
            form = TaskForm()
            context = {'form': form, 'msg': msg}

            return render(request, 'add-task.html', context)

    form = TaskForm()

    context = {'form': form}
    return render(request, 'add-task.html', context)


def daily_task(request):
    user = request.user
    do_task = DailyTask.objects.filter(user=user, do_status=True)
    working_task = DailyTask.objects.filter(user=user, working_status=True)
    done_task = DailyTask.objects.filter(user=user, done_status=True)
    complete_task = DailyTask.objects.filter(
        do_status=False, working_status=False, done_status=False)
    context = {
        'do_task': do_task,
        'working_task': working_task,
        'done_task': done_task,
        'complete_task': complete_task
    }
    return render(request, 'daily-task.html', context)


def move_task(request, id, sts):
    task = DailyTask.objects.get(id=id)
    if sts == 'move working':
        task.working_status = True
        task.do_status = False
        task.save()
        return redirect('daily-task')
    if sts == 'move done':
        task.done_status = True
        task.working_status = False
        task.do_status = False
        task = task.save()
        return redirect('/daily-task')
    if sts == 'done':
        task.done_status = False
        task.working_status = False
        task.do_status = False
        task.save()
        return redirect('/daily-task')
        return redirect('/daily-task')
    return redirect('/daily-task')


def complete_task(request):
    complete_task = DailyTask.objects.filter(
        do_status=False, working_status=False, done_status=False)
    print(complete_task)
    context = {'complete_task': complete_task}
    return render(request, 'daily-task.html', context)

def leave_application(request):
    if request.method=='POST':
        form=LeaveForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form=form.save()
            msg="Application Submitted Please wait for Permission"
            context={
                'form':form,
                'msg': msg
            }
            return render(request, 'leave-form.html', context)

    form=LeaveForm()
    context={
        'form':form
    }
    return render (request,'leave-form.html',context)

def new_application(request):
    application=Leave.objects.filter(check_status=False)
    context={'application':application}
    return render(request,'new-application.html',context)

def process_application(request,id,sts):
    leave=Leave.objects.get(id=id)
    leave.check_status=True
    if sts==1:
        leave.approve_status=True
        leave=leave.save()
        return redirect('/new-application')
    else:
        leave.approve_status=False
        leave=leave.save()
        return redirect('/new-application')
    return redirect('/new-application')

def my_leave(request):
    
    application = Leave.objects.filter(user=request.user, approve_status=True)
    context={
        'application': application
    }
    return render(request,'my-application.html',context)

def holiday(request):
    bd_holidays = holidays.Bangladesh()

    # for ptr in holidays.Bangladesh(years=2022).items():
    context = {
        'bd_holidays ': bd_holidays
    }
    return render(request, 'holiday.html', context)

def create_meeting(request):
    if request.method=="POST":
        form=MeetingForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form=form.save()
            msg='Meeting Shedule Added'
            form=MeetingForm()
            context={'form':form,'msg':msg}
            return render(request,'create-meeting.html',context)
    form=MeetingForm()
    context={'form':form}
    return render(request,'create-meeting.html',context)

def today_meeting(request):
    meeting = Meeting.objects.filter(meeting_date=datetime.datetime.now())
    context={'meeting':meeting}
    return render (request,'meeting.html',context)

def add_client(request):
    form=ClientForm()
    if request.method=='POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            form.save()
            msg='Client added successfully'
            context={
                'form':form,
                'msg':msg
            }
            return redirect('/client')
    form=ClientForm()
    context={'form':form}
    return render(request,'create-client.html',context)

def client(request):
    all_client = Client.objects.all()
    clientfilter = ClientFilter(request.GET, queryset=all_client)
    all_client = clientfilter.qs
    context = {'all_client': all_client, 'clientfilter': clientfilter}
    return render (request,'client.html',context)


def client_delete(request,id):
    client=Client.objects.filter(id=id)
    client=client.delete()
    return redirect('client')

def attendance_view(request):
    employee = Employee.objects.get(user=request.user)
    status = None
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                attended_datetime = str(timezone.now())[:10]
                print(attended_datetime)
            except:
                pass

            attended_today = Attendance.objects.filter(attender=request.user, datetime__startswith=attended_datetime)
            
            if str(attended_today)[10:] == "[]>":
                status = 3

            else:
                status = 2
                msg="Sorry, you can't attend more than once in a day"

            if status == 3:
                attend_object = Attendance(attender=request.user)
                attend_object.save()
                status= 1
                msg="Welcome.Attendance successful"
            return render(request,"attend.html",{'status': status,"employee":employee,'msg':msg})

        else: 
            status = 0
    return render(request, "attend.html", {'status': status,"employee":employee})