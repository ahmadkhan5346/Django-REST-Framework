from rest_framework import serializers
from.models import Teacher

class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    id_no = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Teacher.objects.create(**validate_data)