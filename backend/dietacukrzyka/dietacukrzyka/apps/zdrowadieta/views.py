from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework import permissions, status


from .models import Client
from .serializers import ClientSerializer

@permission_classes((permissions.AllowAny,))
class ClientsView(APIView):

    def get(self, request):
        users = Client.objects.get(name="Yuriy")
        serializer = ClientSerializer(users)
        return Response(serializer.data, status=status.HTTP_200_OK)