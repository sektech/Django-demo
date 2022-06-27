import datetime

from django.http import HttpResponse
from django.shortcuts import render
from demoapp.models import Employee
# Create your views here.

def welcome(request):
    date = datetime.datetime.now()
    date_dict = {'display_date':date,'emp_name': 'Sekar'}

    return render(request,'demoapp/demo.html',context=date_dict)

def loadEmpl(request):
    emp_dic = {'emp_list': Employee.objects.all()}
    return render(request,'demoapp/employee.html',context=emp_dic)
