from rest_framework import serializers
from .models import Manager, Intern, Address

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'first_name', 'last_name', 'email', 'date_joined', 'department']
        read_only_fields = ['id', 'date_joined']

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = ['id', 'first_name', 'last_name', 'email', 'date_joined', 'mentor', 'internship_end']
        read_only_fields = ['id', 'date_joined']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'manager', 'intern', 'street', 'city', 'state', 'zip_code']
        read_only_fields = ['id']
