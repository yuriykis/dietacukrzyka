from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework import permissions, status


from .models import User
from .serializers import UserSerializer

@permission_classes((permissions.AllowAny,))
class UsersView(APIView):

    def get(self, request):
        users = User.objects.get(first_name="Yuriy")
        serializer = UserSerializer(users)
        return Response(serializer.data, status=status.HTTP_200_OK)