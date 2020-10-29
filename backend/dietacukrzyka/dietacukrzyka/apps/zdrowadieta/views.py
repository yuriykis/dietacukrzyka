import os
from . import weights
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework import permissions, status
from django.contrib.auth.models import User as MainUser
from datetime import datetime
from django.http import FileResponse
from django.conf import settings

from .models import *
from .serializers import *
import json


class RegistrationView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(request.data)
        name = serializer.data.get('name')
        last_name = serializer.data.get('last_name')
        age = serializer.data.get('age')
        username = serializer.data.get('username')
        password = serializer.data.get('password')

        if (MainUser.objects.filter(username=username).count() == 0):
            user = MainUser.objects.create_user(
                username=username, password=password)
            new_user = User(user=user)
            new_user.save()

            new_client = Client(user=new_user, name=name,
                                last_name=last_name, age=age)
            new_client.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_409_CONFLICT)


class ClientMenuView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, meal_type, menu_date):
        if(int(meal_type) > 5):
            return Response(status=status.HTTP_404_NOT_FOUND)
        main_user = MainUser.objects.get(username=request.user)
        user = User.objects.get(user=main_user)
        client = Client.objects.get(user=user)
        client_menu = ClientMenu.objects.get(client=client)
        menu = Menu.objects.get(id=client_menu.menu_id)
        meals = list(Meal.objects.filter(
            menu=menu, date=datetime.datetime.strptime(menu_date, '%Y-%m-%d').date()))
        recipe = Recipe.objects.get(id=meals[int(meal_type)].recipe_id)
        rec_ingredient = RecipeIngredient.objects.filter(recipe=recipe)
        ingredients = []
        for i in rec_ingredient:
            ingredients.append(i.ingredient.name)

        response = {
            'name': recipe.name,
            'method': recipe.method,
            'type': recipe.type,
            'calories': meals[int(meal_type)].calories,
            'date': meals[int(meal_type)].date
        }
        return Response(response)


class ClientMenuView1(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        dates_response = []
        menu_dates = [
            '2020-10-12',
            '2020-10-13',
            '2020-10-14',
            '2020-10-15',
            '2020-10-16',
            '2020-10-17',
            '2020-10-18',
        ]
        dates_response = []
        for date_index in range(6):
            meals_response = []
            for meal_type in range(5):
                main_user = MainUser.objects.get(username=request.user)
                user = User.objects.get(user=main_user)
                client = Client.objects.get(user=user)
                client_menu = ClientMenu.objects.get(client=client)
                menu = Menu.objects.get(id=client_menu.menu_id)
                meals = list(Meal.objects.filter(
                    menu=menu, date=datetime.datetime.strptime(menu_dates[date_index], '%Y-%m-%d').date()))
                recipe = Recipe.objects.get(id=meals[int(meal_type)].recipe_id)
                rec_ingredient = RecipeIngredient.objects.filter(recipe=recipe)

                ingredients = []
                for i in rec_ingredient:
                    ingredients.append(i.ingredient.name)

                ingredients_cal = []
                ingredients_mass_factors = []
                for i in rec_ingredient:
                    ingredients_cal.append(i.ingredient.calories)
                    ingredients_mass_factors.append(i.massFraction)
                client_info = []
                client_info.append(client.age)
                client_info.append(client.weight)
                client_info.append(client.height)
                client_info.append(client.gender)
                weights_info = weights.main(
                    ingredients_cal, ingredients_mass_factors, client_info, meal_type)

                recipe_data = {
                    'name': recipe.name,
                    'method': recipe.method,
                    'type': recipe.type,
                    'calories': meals[int(meal_type)].calories,
                    'date': meals[int(meal_type)].date,
                    'ingredients': ingredients,
                    'weights_info': weights_info
                }
                meals_response.append(recipe_data)
            dates_response.append(meals_response)
        return Response(dates_response)


class ClientMenuIngredientsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, meal_type, menu_date):
        if(int(meal_type) > 5):
            return Response(status=status.HTTP_404_NOT_FOUND)
        main_user = MainUser.objects.get(username=request.user)
        user = User.objects.get(user=main_user)
        client = Client.objects.get(user=user)
        client_menu = ClientMenu.objects.get(client=client)
        menu = Menu.objects.get(id=client_menu.menu_id)
        meals = list(Meal.objects.filter(
            menu=menu, date=datetime.datetime.strptime(menu_date, '%Y-%m-%d').date()))
        recipe = Recipe.objects.get(id=meals[int(meal_type)].recipe_id)
        rec_ingredient = RecipeIngredient.objects.filter(recipe=recipe)
        ingredients = []
        for i in rec_ingredient:
            ingredients.append(i.ingredient.name)

        return Response(json.dumps(ingredients))


class ClientGenerateIngredientsWeight(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, meal_type, menu_date):
        if(int(meal_type) > 5):
            return Response(status=status.HTTP_404_NOT_FOUND)
        main_user = MainUser.objects.get(username=request.user)
        user = User.objects.get(user=main_user)
        client = Client.objects.get(user=user)
        client_menu = ClientMenu.objects.get(client=client)
        menu = Menu.objects.get(id=client_menu.menu_id)
        meals = list(Meal.objects.filter(
            menu=menu, date=datetime.datetime.strptime(menu_date, '%Y-%m-%d').date()))
        recipe = Recipe.objects.get(id=meals[int(meal_type)].recipe_id)
        rec_ingredient = RecipeIngredient.objects.filter(recipe=recipe)
        ingredients_cal = []
        ingredients_mass_factors = []
        for i in rec_ingredient:
            ingredients_cal.append(i.ingredient.calories)
            ingredients_mass_factors.append(i.massFraction)
        client_info = []
        client_info.append(client.age)
        client_info.append(client.weight)
        client_info.append(client.height)
        client_info.append(client.gender)
        weights_info = weights.main(
            ingredients_cal, ingredients_mass_factors, client_info, meal_type)
        return Response(json.dumps(weights_info))


class ClientDataGetView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        main_user = MainUser.objects.get(username=request.user)
        user = User.objects.get(user=main_user)
        client = Client.objects.get(user=user)

        response = {
            'login': main_user.username,
            'email': main_user.email,
            'name': client.name,
            'last_name': client.last_name,
            'weight': client.weight,
            'height': client.height,
            'age': client.age
        }

        return Response(response)


class ClientDataSaveView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        serializer = ClientDataSerializer(request.data)
        email = serializer.data.get('email')
        name = serializer.data.get('name')
        last_name = serializer.data.get('last_name')
        weight = serializer.data.get('weight')
        height = serializer.data.get('height')
        age = serializer.data.get('age')

        main_user = MainUser.objects.get(username=request.user)
        user = User.objects.get(user=main_user)
        client = Client.objects.get(user=user)

        if (email and MainUser.objects.filter(email=email).count() != 0):
            return Response(status=status.HTTP_409_CONFLICT)
        else:
            main_user.email = email
            client.name = name
            client.last_name = last_name
            client.weight = weight
            client.height = height
            client.age = age

            main_user.save()
            client.save()

            return Response(status=status.HTTP_200_OK)


class FileDownloader(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, file):
        try:
            meals_folder = os.path.join(settings.IMAGES_DIR, "Dania")
            results_folder = os.path.join(meals_folder, file)
            return FileResponse(open(results_folder, 'rb'))
        except FileNotFoundError:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
