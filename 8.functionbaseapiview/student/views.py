from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from. serializers import StudentSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            std = Student.objects.get(id = id)
            serializer = StudentSerializer(std)
            return Response(serializer.data)

        std = Student.objects.all()
        serializer = StudentSerializer(std, many=True)
        return Response(serializer.data)

        # return Response({'msg': 'This is GET request'})


    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    #     print(request.data)
    #     return Response({'msg': 'This is POST request', 'data':request.data})


    if request.method == 'PUT':
        id = pk
        std = Student.objects.get(pk=id)
        serializer = StudentSerializer(std, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'PATCH':
        id = pk
        std = Student.objects.get(pk=id)
        serializer = StudentSerializer(std, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response({'msg':'Partial Data Updated'})




    if request.method == 'DELETE':
        id = pk
        # id = request.data.get('id')
        std = Student.objects.get(pk=id)
        std.delete()
        return Response({'msg':'Data Deleted'})


    