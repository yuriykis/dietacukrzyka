from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    """User"""

    class Meta:
        model = User
        fields = ("first_name", "last_name")
