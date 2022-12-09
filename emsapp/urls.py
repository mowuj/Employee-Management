
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('login', user_login, name='login'),
    path('signup', create_user, name='signup'),
    path('add-employee', add_employee, name='add-employee'),
    path('all-employee', all_employee, name='all-employee'),
    path('delete/<int:id>', delete, name='delete'),
    path('detail/<int:id>', employee_detail, name='detail'),
    path('profile', profile, name='profile'),
    path('profile-detail/<int:id>', profile_detail, name='profile-detail'),
    path('edit-profile/<int:id>', edit_profile, name='edit-profile'),
    path('daily-task', daily_task, name='daily-task'),
    path('add-task', add_task, name='add-task'),
    path('move-task/<int:id>/<sts>', move_task, name='move-task'),
    
]
