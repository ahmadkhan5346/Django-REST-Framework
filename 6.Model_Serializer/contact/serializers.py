from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    # Validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name Should be start with R')
    name = serializers.CharField(read_only = True)

    class Meta:
        model = Contact
        fields = '__all__'
        # read_only_fields = ['name', 'roll']
        # extra_kwargs = {'name':{'read_only':True}}

        # Validators
# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError('Name Should be start with R')
# name = serializers.CharField(read_only = True)