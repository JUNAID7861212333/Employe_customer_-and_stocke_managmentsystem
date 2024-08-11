from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Attendance, Salary,SalaryDetection
from .forms import EmployeeForm, AttendanceForm

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})

def attendance_entry(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            # Save data to corresponding month and year folder
            return redirect('attendance_entry')
    else:
        form = AttendanceForm()
    return render(request, 'attendance_entry.html', {'form': form})

def monthly_summary(request, month, year):
    # Process data and calculate salary deductions
    data = []
    employees = Employee.objects.all()
    for employee in employees:
        absences = Attendance.objects.filter(employee=employee, date__month=month, date__year=year, absent=True).count()
        late_arrivals = Attendance.objects.filter(employee=employee, date__month=month, date__year=year, late=True).count()
        presents = Attendance.objects.filter(employee=employee, date__month=month, date__year=year, present=True).count()
        leaves = Attendance.objects.filter(employee=employee, date__month=month, date__year=year, on_leave=True).count()
        original_salary = employee.salary
        deductions = absences * 100 + late_arrivals * 50
        remaining_salary = original_salary - deductions
        
        data.append({
            'name': employee.name,
            'department': employee.designation,
            'original_salary': original_salary,
            'absences': absences,
            'late_arrivals': late_arrivals,
            'presents': presents,
            'leaves': leaves,
            'deductions': deductions,
            'remaining_salary': remaining_salary,
        })

    return render(request, 'monthly_summary.html', {'data': data})










# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Employee, Attendance

# def monthly_summary(request, month, year):
#     data = []
#     number_leave = 10
#     number_absent = 10
    
#     if request.method == 'POST':
#         # Get the number inputs from the form
#         number_leave = int(request.POST.get('detect_number_onleave', 0))
#         number_absent = int(request.POST.get('detect_number_onlate', 0))

#     employees = Employee.objects.all()
#     for employee in employees:
#         absences = Attendance.objects.filter(employee=employee, date__month=month, date__year=year, absent=True).count()
#         late_arrivals = Attendance.objects.filter(employee=employee, date__month=month, date__year=year, late=True).count()
#         presents = Attendance.objects.filter(employee=employee, date__month=month, date__year=year, present=True).count()
#         leaves = Attendance.objects.filter(employee=employee, date__month=month, date__year=year, on_leave=True).count()
#         original_salary = employee.salary
#         deductions = absences * number_absent + late_arrivals * number_leave
#         remaining_salary = original_salary - deductions
        
#         data.append({
#             'name': employee.name,
#             'department': employee.designation,
#             'original_salary': original_salary,
#             'absences': absences,
#             'late_arrivals': late_arrivals,
#             'presents': presents,
#             'leaves': leaves,
#             'deductions': deductions,
#             'remaining_salary': remaining_salary,
#         })

#     return render(request, 'monthly_summary.html', {'data': data, 'number_leave': number_leave, 'number_absent': number_absent})


from django.shortcuts import render, redirect
from .forms import AttendanceForm

def save_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_entry')  # Redirect to the attendance entry page after saving
    # Handle invalid form or GET request if needed
    return redirect('attendance_entry')  # Redirect to attendance entry in case of errors


from django.shortcuts import render
from .models import Attendance

def show_attendance(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'attendances': attendances})


from django.shortcuts import render, redirect
from .forms import MonthYearForm

def select_month_year(request):
    if request.method == 'POST':
        form = MonthYearForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            return redirect('employee_summary', month=month, year=year)
    else:
        form = MonthYearForm()
    
    return render(request, 'select_month_year.html', {'form': form})



from django.shortcuts import render
from .models import Employee, Attendance





from django.shortcuts import render, get_object_or_404
from .models import Employee, Attendance





# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import SalaryDetection

def update_salary_detection(request, pk):
    salary_detection = get_object_or_404(SalaryDetection, pk=pk)
    
    if request.method == 'POST':
        detect_on_absent = request.POST.get('detect_on_absent')
        detect_on_late = request.POST.get('detect_on_late')
        
        if detect_on_absent is not None and detect_on_late is not None:
            salary_detection.detect_on_absent = detect_on_absent
            salary_detection.detect_on_late = detect_on_late
            salary_detection.save()
            return redirect('success_view')  # Redirect to a success page or list view
    
    return render(request, 'update_salary_detection.html', {'salary_detection': salary_detection})



# from django.shortcuts import render, get_object_or_404
# from .models import Employee, Attendance

# def employee_summary(request, month, year):
    
#     employees = Employee.objects.all()
#     data = []
#     for employee in employees:
#         absences = Attendance.objects.filter(employee=employee, date__month=month, date__year=year, absent=True).count()
#         late_arrivals = Attendance.objects.filter(employee=employee, date__month=month, date__year=year, late=True).count()
#         original_salary = employee.salary
        
#         deductions = absences * 100 + late_arrivals * 50
#         # deductions = absences * SalaryDetection.detect_on_absent + late_arrivals * SalaryDetection.detect_on_late
#         remaining_salary = original_salary - deductions

#         data.append({
#             'id': employee.id,
#             'name': employee.name,
#             'department': employee.designation,
#             'original_salary': original_salary,
#             'absences': absences,
#             'late_arrivals': late_arrivals,
#             'deductions': deductions,
#             'remaining_salary': remaining_salary,
#         })

#     return render(request, 'employee_summary.html', {'data': data, 'month': month, 'year': year})





from django.shortcuts import render, get_object_or_404
from .models import Employee, Attendance, SalaryDetection

def employee_summary(request, month, year):
    try:
        salary_detection = SalaryDetection.objects.first()
        if not salary_detection:
            return render(request, 'error.html', {'message': 'No SalaryDetection data available. Please add SalaryDetection data.'})
    except SalaryDetection.DoesNotExist:
        return render(request, 'error.html', {'message': 'No SalaryDetection data available. Please add SalaryDetection data.'})

    detect_on_absent = salary_detection.detect_on_absent
    detect_on_late = salary_detection.detect_on_late

    employees = Employee.objects.all()
    data = []
    for employee in employees:
        absences = Attendance.objects.filter(employee=employee, date__month=month, date__year=year, absent=True).count()
        late_arrivals = Attendance.objects.filter(employee=employee, date__month=month, date__year=year, late=True).count()
        original_salary = employee.salary
        
        deductions = absences * detect_on_absent + late_arrivals * detect_on_late
        remaining_salary = original_salary - deductions

        data.append({
            'id': employee.id,
            'name': employee.name,
            'department': employee.designation,
            'original_salary': original_salary,
            'absences': absences,
            'late_arrivals': late_arrivals,
            'deductions': deductions,
            'remaining_salary': remaining_salary,
        })

    return render(request, 'employee_summary.html', {'data': data, 'month': month, 'year': year})





def attendance_details(request, employee_id, month, year):
    employee = get_object_or_404(Employee, id=employee_id)
    attendances = Attendance.objects.filter(employee=employee, date__month=month, date__year=year)
    return render(request, 'attendance_details.html', {'employee': employee, 'attendances': attendances})




# ///////////////////////////////////////////////////////
# views.py




# views.py

