from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Students


@api_view(['GET','POST'])
def list_post(request):
    
    if request.method == 'GET':
        all_students = Students.objects.all()
        serializer = StudentSerializer(all_students,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        new_student = StudentSerializer(data=request.data)
        if new_student.is_valid():
            new_student.save()
            return Response(new_student.data,status.HTTP_201_CREATED)
        return Response(new_student.errors,status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','DELETE'])
def posts_details(request,id):
    try:
        student = Students.objects.get(id=id)
    except Students.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method == 'DELETE':
        student.delete()
        return Response(status.HTTP_204_NO_CONTENT)