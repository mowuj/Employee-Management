from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import messages
# from django.contrib.auth.decorators import login_require
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from .forms import *
from .filters import *
from django.db.models import Sum, Q
import datetime
from datetime import date
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


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
            current_site=get_current_site(request)
            mail_subject='An account Created'
            message=render_to_string('account.html',{
                'user':user_form,
                'domain':current_site.domain

            })
            send_mail=form.cleaned_data.get('email')
            email=EmailMessage(mail_subject,message,to=[send_mail])
            email.send()
            print('send')
            messages.success(request, 'Successfully Account Created !')
            return redirect('/all-employee')
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

def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            update_session_auth_hash(request,form.user)
            messages.success(request,'Password has successfully Changed')
            return redirect('home')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'change-password.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    employee=Employee.objects.all()
    dept=Department.objects.all()
    post=Post.objects.all()
    leave=Leave.objects.filter(end_date__gte =datetime.date.today())
    do_task=DailyTask.objects.filter(do_status=True)
    working_task=DailyTask.objects.filter(working_status=True)
    done_task=DailyTask.objects.filter(done_status=True)

    meeting=Meeting.objects.filter(meeting_date=datetime.datetime.now())
    client=Client.objects.all()
    attend=Attendance.objects.filter(datetime__date=datetime.datetime.now())
    context={'employee':employee,
            'dept':dept,'post':post,
            'leave':leave,
            'do_task':do_task,
            'working_task':working_task,
            'done_task': done_task,
            'meeting':meeting,
            'client':client,'attend':attend}
    return render(request, 'home.html',context)


def department(request):
    all_dept=Department.objects.all()
    return render(request,'department.html',{'all_dept':all_dept})

def add_department(request):
    form=DepartmentAddForm()
    if request.method=='POST':
        form=DepartmentAddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            context={'form':form}
            return redirect('department')
    form = DepartmentAddForm()
    context = {'form': form}
    return render(request, 'add_department.html', context)

def edit_department(request,id):
    department = Department.objects.get(id=id)
    form = DepartmentAddForm(instance=department)
    if request.method == 'POST':
        form = DepartmentAddForm(request.POST, request.FILES,instance=department)
        if form.is_valid():
            form.save()
            return redirect('department')
    context = {'form': form}
    return render(request, 'edit-department.html', context)

def post(request):
    all_post=Post.objects.all()
    return render(request,'post.html',{'all_post':all_post})

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
    department = profile.department
    dept = Employee.objects.filter(department=department)
    context = {'profile': profile,'dept':dept }
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

def today_leave(request):
    today_leave = Leave.objects.filter(approve_status=True,end_date__gte =datetime.date.today())
    print(today_leave)
    return render(request,'today-leave.html',{'today_leave':today_leave})

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
            msg='Meeting Schedule Added'
            form=MeetingForm()
            context={'form':form,'msg':msg}
            return render(request,'create-meeting.html',context)
    form=MeetingForm()
    context={'form':form}
    return render(request,'create-meeting.html',context)

def today_meeting(request):
    meeting = Meeting.objects.filter(meeting_date=datetime.datetime.today())
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
    attendance=Attendance.objects.all()
    status = None
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                attended_datetime = str(timezone.now())[:10]
                
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
            return render(request,"attend.html",{'status': status,"employee":employee,'msg':msg,"attendance":attendance})

        else: 
            status = 0
    return render(request, "attend.html", {'status': status,"employee":employee})

def attendance_report(request):
    attend=Attendance.objects.filter(datetime__date=datetime.datetime.today())
    print(attend)
    # all_attend = Attendance.objects.all()
    # attendfilter = AttendFilter(request.GET, queryset=all_attend)
    # all_attend = attendfilter.qs
    return render(request,'report.html',{'attend':attend})