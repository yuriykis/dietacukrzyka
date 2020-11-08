from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from .models import Client


class RegistrationSerializer(serializers.Serializer):
    """Registration"""

    name = serializers.CharField()
    last_name = serializers.CharField()
    age = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField()


class ClientDataSerializer(serializers.Serializer):

    name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    weight = serializers.IntegerField()
    height = serializers.IntegerField()
    age = serializers.IntegerField()
    gender = serializers.CharField()
    preferred_ingredients = serializers.ListField(
        child=serializers.CharField())
    standard_ingredients = serializers.ListField(child=serializers.CharField())
    allergens = serializers.ListField(child=serializers.CharField())
