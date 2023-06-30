
from django.urls import path
from .views import post_employee, get_employee, get_sorted_employees

urlpatterns = [
    path('employees/', post_employee, name='post_employee'),
    path('employees/<int:employee_id>/', get_employee, name='get_employee'),
    path('employees/sort_by_salary/', get_sorted_employees, name='get_sorted_employees'),
]