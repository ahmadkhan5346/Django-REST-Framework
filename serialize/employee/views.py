from sqlite3 import DatabaseError
from django.shortcuts import render
from.models import Employee
from.serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.
# Model object - Singal Employee Data

# Query Set - One Employee data
def employee_details(request,kk):
    emp = Employee.objects.get(id=kk)                            # This is a complex data
    serializer = EmployeeSerializer(emp)                         #  complex data convert in python object
    # jsondata = JSONRenderer().render(serializer.data)          #  python object convert in json
    # return HttpResponse(jsondata, content_type='application/json')
    return JsonResponse(serializer.data)



def employee_list(request):
    emp = Employee.objects.all() # This is a complex data
    serializer = EmployeeSerializer(emp, many=True)             #  complex data convert in python object
    # jsondata = JSONRenderer().render(serializer.data)         #  python object convert in json
    # return HttpResponse(jsondata, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)




