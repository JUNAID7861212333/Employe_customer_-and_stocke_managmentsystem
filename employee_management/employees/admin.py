from django.contrib import admin
from .models import Employee, Attendance, Salary, SalaryDetection

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fullname', 'age', 'blood_group', 'designation',
                    'phone_number', 'photo', 'salary', 'joining_date', 'department',
                    'gender', 'email', 'date_of_birth', 'description', 'whatsapp',
                    'sms', 'idcard')
    search_fields = ('name', 'designation', 'department', 'email', 'phone_number')
    list_filter = ('designation', 'department', 'gender', 'joining_date')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'date', 'present', 'absent', 'on_leave', 'late', 'on_time')
    list_filter = ('present', 'absent', 'on_leave', 'late', 'on_time')
    search_fields = ('employee__name',)

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'month', 'year', 'original_salary', 'absences', 'late_arrivals',
                    'presents', 'leaves', 'deductions', 'remaining_salary')
    list_filter = ('month', 'year')
    search_fields = ('employee__name',)

@admin.register(SalaryDetection)
class SalaryDetectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'detect_on_absent', 'detect_on_late')

