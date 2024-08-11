from django import forms
from .models import Employee, Attendance

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','fullname', 'age', 'blood_group', 'designation', 'phone_number', 'photo', 'salary','idcard','sms','whatsapp','description','date_of_birth','email','gender']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'present', 'absent', 'on_leave', 'late', 'on_time']





class MonthYearForm(forms.Form):
    MONTH_CHOICES = [
        ('1', 'January'),
        ('2', 'February'),
        ('3', 'March'),
        ('4', 'April'),
        ('5', 'May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    ]

    year = forms.IntegerField(label='Year', min_value=2000, max_value=2050)
    month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES)





