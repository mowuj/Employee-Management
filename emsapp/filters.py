import django_filters
from django_filters import DateFilter,CharFilter
from .models import *

class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model=Employee
        fields='__all__'
        exclude=[
            'phone',
            'nid',
            'ssc',
            'hsc',
            'honors',
            'masters',
            'salary',
            'email',
            'image',
            'father_name',
            'mother_name'
        ]
