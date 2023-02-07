
from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
urlpatterns = [
    # path('chart',sales_view,name='chart'),
    path('reset/password/', PasswordResetView.as_view(template_name='reset_pass.html'), name='password_reset'),

    path('reset/password/done/', PasswordResetDoneView.as_view(
        template_name='reset_pass_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(
        template_name='pass_reset_confirm.html'), name='password_reset_confirm'),

    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='pass_reset_complete.html'), name='password_reset_complete'),
    path('login', user_login, name='login'),
    path('signup', create_user, name='signup'),
    path('change-pass', change_password, name='change-pass'),
    path('logout', user_logout, name='logout'),
    path('',home,name='home'),
    path('add-employee', add_employee, name='add-employee'),
    path('department',department,name='department'),
    path('add-department',add_department,name='add-department'),
    path('edit-department/<int:id>',edit_department,name='edit-department'),
    path('all-employee', all_employee, name='all-employee'),
    path('delete/<int:id>', delete, name='delete'),
    path('detail/<int:id>', employee_detail, name='detail'),
    path('profile', profile, name='profile'),
    path('profile-detail/<int:id>', profile_detail, name='profile-detail'),
    path('edit-profile/<int:id>', edit_profile, name='edit-profile'),
    path('daily-task', daily_task, name='daily-task'),
    path('complete-task', complete_task, name='complete-task'),
    path('add-task', add_task, name='add-task'),
    path('move-task/<int:id>/<sts>', move_task, name='move-task'),
    path('leave-application', leave_application, name='leave-application'),
    path('new-application', new_application, name='new-application'),
    path('process-application/<int:id>/<int:sts>', process_application, name='process-application'),
    path('my-leave', my_leave, name='my-leave'),
    path('today-leave', today_leave, name='today-leave'),
    path('create-meeting', create_meeting, name='create-meeting'),
    path('meeting', today_meeting, name='meeting'),
    path('add-client', add_client, name='add-client'),
    path('client', client, name='client'),
    path('client-delete/<int:id>', client_delete, name='client-delete'),
    path('attendance', attendance_view, name='attendance'),
    path('report', attendance_report, name='report'),
]
