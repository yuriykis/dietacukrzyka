from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework import permissions, status
from django.contrib.auth.models import User as MainUser


from .models import *
from .serializers import *


class RegistrationView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(request.data)
        name = serializer.data.get('name')
        last_name = serializer.data.get('last_name')
        age = serializer.data.get('age')
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        
        if (MainUser.objects.filter(username = username).count() == 0):
            user = MainUser.objects.create_user(username = username, password = password)
            new_user = User(user = user)
            new_user.save()

            new_client = Client(user = new_user, name = name, last_name = last_name, age = age)
            new_client.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_409_CONFLICT)


class ClientMenuView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, meal_type):
        if(int(meal_type) > 4):
            return Response(status=status.HTTP_404_NOT_FOUND)
        main_user = MainUser.objects.get(username = request.user)
        user = User.objects.get(user = main_user)
        client = Client.objects.get(user = user)
        client_menu = ClientMenu.objects.get(client = client)
        menu = Menu.objects.get(id = client_menu.menu_id)
        meals = list(Meal.objects.filter(menu = menu))
        recipe = Recipe.objects.get(id = meals[int(meal_type)].recipe_id)

        response = {
            'name': recipe.name,
            'method': recipe.method,
            'type': recipe.type,
            'calories': meals[int(meal_type)].calories,
            'date': meals[int(meal_type)].date
        }

        return Response(response)
