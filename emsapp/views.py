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


# Create your views here.
def home(request):
    return render(request, 'home.html')

# def create_user(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             employee = Employee.objects.create()

#             # messages.success(request, 'Successfully created account')

#             return redirect('login')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


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


def delete(request):
    remove = Employee.objects.get(id=id)
    remove = remove.delete()
    return ('/all-employee')


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
# def today_leaving(request):
#     today = datetime.datetime.now()
    
#     leave = Leave.object.filter(approve_status=True)
    
def my_leave(request):
    
    application = Leave.objects.filter(user=request.user, approve_status=True)
    context={
        'application': application
    }
    return render(request,'my-application.html',context)

# def holiday(request):
#     uk_holidays = holidays.Bangladesh()


# # Print all the holidays in UnitedKingdom in year 2018
# for ptr in holidays.Bangladesh(years=2022).items():
#     print(ptr)
# from django.views import generic
# from django.utils.safestring import mark_safe
# from .utils import Calendar
# from django.http import HttpResponse, HttpResponseRedirect
# import calendar
# from datetime import datetime, timedelta, date
# class CalendarView(generic.ListView):
#     model = Event
#     template_name = 'calendar.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         d = get_date(self.request.GET.get('month', None))
#         cal = Calendar(d.year, d.month)
#         html_cal = cal.formatmonth(withyear=True)
#         context['calendar'] = mark_safe(html_cal)
#         context['prev_month'] = prev_month(d)
#         context['next_month'] = next_month(d)
#         return context

# def get_date(req_month):
#     if req_month:
#         year, month = (int(x) for x in req_month.split('-'))
#         return date(year, month, day=1)
#     return datetime.today()

# def prev_month(d):
#     first = d.replace(day=1)
#     prev_month = first - timedelta(days=1)
#     month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
#     return month

# def next_month(d):
#     days_in_month = calendar.monthrange(d.year, d.month)[1]
#     last = d.replace(day=days_in_month)
#     next_month = last + timedelta(days=1)
#     month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
#     return month

# def event(request, event_id=None):
#     instance = Event()
#     if event_id:
#         instance = get_object_or_404(Event, pk=event_id)
#     else:
#         instance = Event()

#     form = EventForm(request.POST or None, instance=instance)
#     if request.POST and form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse('calendar'))
#     return render(request, 'event.html', {'form': form})