from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    mobile = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)