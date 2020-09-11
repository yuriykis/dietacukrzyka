from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from .models import Client

class RegistrationSerializer(serializers.Serializer):
    """Registration"""

    name = serializers.CharField()
    last_name = serializers.CharField()
    age = serializers.IntegerField()
    login = serializers.CharField()
    password = serializers.CharField()


