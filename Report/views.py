from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .email import *

def display(request):
    q=Employee.objects.all()
    return render(request,'Report/details.html',{'q':q})

def mailing(request):
    q=Employee.objects.all()
    str1= ""
    for i in q:
        str1=str1+(f"Employee ID: {i.staffId}, Employee Name: {i.staffName}, Designation: {i.Designation} and Salary: {i.Salary}\n")

    sendemail(str1)
    return HttpResponse("Email Sent!")
