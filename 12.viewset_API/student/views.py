from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets
from student import serializers


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print('*******List********')
        print('Basename:', self.basename)
        print('Action:', self.action)
        print('Details:', self.detail)
        print('Suffix:', self.suffix)
        print('Name:', self.name)
        print('Description:', self.description)
        std = Student.objects.all()
        serializer = StudentSerializer(std, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        # if id is not None:
        std = Student.objects.get(pk=id)
        serializer = StudentSerializer(std)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        std = Student.objects.get(id=pk)
        serializer = StudentSerializer(std, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        std = Student.objects.get(pk=pk)
        serializer = StudentSerializer(std, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        std = Student.objects.get(id=id)
        std.delete()
        return Response({'msg':'Data Deleted'})

