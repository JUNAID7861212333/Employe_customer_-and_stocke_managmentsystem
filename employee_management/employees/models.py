from django.db import models

from django.db import models
from datetime import date

class Employee(models.Model):
    name = models.CharField(max_length=100)
    fullname = models.CharField(max_length=200)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=10)
    designation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='photos/')
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField(default=date.today)  # Set default to today's date
    department = models.CharField(max_length=100, default='General')  # Default department
    gender = models.CharField(max_length=10, default='Not Specified')  # Default gender
    email = models.EmailField(default='example@example.com')  # Default email
    date_of_birth = models.DateField(default=date(2000, 1, 1))  # Default DOB
    description = models.TextField(default='No description provided')  # Default description
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    sms = models.CharField(max_length=15, blank=True, null=True)
    idcard = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)
    absent = models.BooleanField(default=False)
    on_leave = models.BooleanField(default=False)
    late = models.BooleanField(default=False)
    on_time = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_salaries')
    month = models.IntegerField()
    year = models.IntegerField()
    original_salary = models.DecimalField(max_digits=10, decimal_places=2)
    absences = models.IntegerField(default=0)
    late_arrivals = models.IntegerField(default=0)
    presents = models.IntegerField(default=0)
    leaves = models.IntegerField(default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    remaining_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.employee.name} - {self.month}/{self.year}"


from django.db import models

class SalaryDetection(models.Model):
    detect_on_absent = models.IntegerField()
    detect_on_late = models.IntegerField()
