from rest_framework import serializers

from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    """Client"""

    class Meta:
        model = Client
        fields = ("user_id", "name", "last_name", "weight", "height")
