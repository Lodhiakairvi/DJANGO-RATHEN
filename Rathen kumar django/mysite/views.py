from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee
def home(request):

    emp_data = Employee.objects.all( )
    print(emp_data) #To print data in terminal
    context = {
        'employees': emp_data,
    }
    return render(request,'home.html' , context)