from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class UsersView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users)
        return Response(serializer.data)