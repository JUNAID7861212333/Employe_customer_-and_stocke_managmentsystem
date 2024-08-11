from django.urls import path
from . import views

urlpatterns = [
    # Employee URLs
    path('', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/update/<int:pk>/', views.employee_update, name='employee_update'),
    path('employees/delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('employees/attendance/', views.attendance_entry, name='attendance_entry'),
    path('employees/summary/<int:month>/<int:year>/', views.monthly_summary, name='monthly_summary'),
    path('employees/attendance/save/', views.save_attendance, name='save_attendance'),
    path('employees/attendance/show/', views.show_attendance, name='show_attendance'),
    path('employees/select_month_year/', views.select_month_year, name='select_month_year'),
    path('employees/employee_summary/<int:month>/<int:year>/', views.employee_summary, name='employee_summary'),
    path('employees/attendance_details/<int:employee_id>/<int:month>/<int:year>/', views.attendance_details, name='attendance_details'),

    
]
