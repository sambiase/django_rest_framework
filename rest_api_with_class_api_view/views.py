from rest_framework.views import APIView
from .models import Employees
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status

class ListEmployeesAPIView (APIView):

    def get (self,request):
        employees = Employees.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post (self,request):
        new_employee = request.data
        serializer = EmployeeSerializer(data=new_employee)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class DetailEmployeesAPIView (APIView):
    def get_object (self,pk):
        try: 
            return Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def get(self,request, pk):
        employees = self.get_object(pk)
        serializer = EmployeeSerializer(employees)
        return Response(serializer.data,status.HTTP_200_OK)

    def put (self,request,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status.HTTP_204_NO_CONTENT)


