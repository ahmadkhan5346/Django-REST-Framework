from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from student.customauth import CustomaAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [CustomaAuthentication]

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class StudentROMVS(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer