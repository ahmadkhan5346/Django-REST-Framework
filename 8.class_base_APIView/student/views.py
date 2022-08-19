from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from. serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView


class StudentApi(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            std = Student.objects.get(id = id)
            serializer = StudentSerializer(std)
            return Response(serializer.data)

        std = Student.objects.all()
        serializer = StudentSerializer(std, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


    def put(self, request, pk, format=None):
        id = pk
        std = Student.objects.get(pk=id)
        serializer = StudentSerializer(std, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):
        id = pk
        std = Student.objects.get(pk=id)
        serializer = StudentSerializer(std, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
        


    def delete(self, request, pk, format=None):
        id = pk
        std = Student.objects.get(pk=id)
        std.delete()
        return Response({'msg':'Data Deleted'})


    