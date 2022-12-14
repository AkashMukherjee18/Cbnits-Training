from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView

# from . models import Employees
# from . serializers import EmployeesSerializer

# Create your views here.


# class EmployeeList(APIView):
#     def get(self, request):
#         employee1 = Employees.objects.all()
#         serializer = EmployeesSerializer(employee1, many=True)
#         return Response(serializer.data)

#     def post(self):
#         pass

def Index(request):
    return HttpResponse("Hello world! 100")
    
def Index2(request):
    return render(request,"hello.html", {'name' : 'Subho'})

