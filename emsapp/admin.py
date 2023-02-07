from django.contrib import admin
from .models import *

# class DistrictAdmin(admin.ModelAdmin):
#     model=District
#     list_display = ['name','division']

class EmployeeAdmin(admin.ModelAdmin):
    model=Employee
    list_display = ['name',
                    'employee_id',
                    'department',
                    'district',
                    'salary',
                    'email',
                    'phone'
                    ,'father_name',
                    'mother_name']
    list_editable=['salary']


class LeaveAdmin(admin.ModelAdmin):
    model=District
    list_display = ['user',
                    'cause_of_leave',
                    'start_date',
                    'end_date',
                    'check_status',
                    'approve_status']
    list_editable = ['check_status','approve_status']

# class HolidayAdmin(admin.ModelAdmin):
#     model=District
#     list_display = ['Description','start_date','Description']

class DailyTaskAdmin(admin.ModelAdmin):
    model=DailyTask 
    list_display = ['user',
                    'title',
                    'issue_date',
                    'delivery',
                    'working_status',
                    'do_status',
                    'done_status',
                    ]

class DepartmentAdmin(admin.ModelAdmin):
    model=Department
    list_display=[
        'name',
        'manager',
        'start_date',
        
    ]
    list_editable=['manager']

class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ['client_name',
                    'client_id',
                    'email',
                    'phone',
                    'company_name',
                    
                    ]
    
# class MeetingAdmin(admin.ModelAdmin):
#     model = Meeting
#     list_display = ['user',
#                     'name',
#                     'person_with',
#                     ]
#     list_editable=['name','person_with']

# Register your models here.
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Division)
admin.site.register(Post)
admin.site.register(Meeting)
admin.site.register(District)
admin.site.register(Leave,LeaveAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Holiday)
admin.site.register(DailyTask,DailyTaskAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Attendance)
