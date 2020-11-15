import os
from . import weights
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework import permissions, status
from django.contrib.auth.models import User as MainUser
from datetime import datetime, date, timedelta
from django.http import FileResponse
from django.conf import settings

from .models import *
from .serializers import *
import json
import random


class RegistrationView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(request.data)
        name = serializer.data.get('name')
        last_name = serializer.data.get('last_name')
        age = serializer.data.get('age')
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        gender = serializer.data.get('gender')

        if (MainUser.objects.filter(username=username).count() == 0):
            user = MainUser.objects.create_user(
                username=username, password=password)
            new_user = User(user=user)
            new_user.save()

            new_client = Client(user=new_user, name=name,
                                last_name=last_name, age=age, gender=gender)
            new_client.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_409_CONFLICT)


class ClientMenuView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        dates_response = []

        menu_dates = []

        actual_day = datetime.date.today()
        first_day = actual_day
        index = 0
        while not first_day.weekday() == 0:
            index = index + 1
            first_day = actual_day - timedelta(days=index)

        menu_dates_test = []
        actual_day = first_day
        for i in range(0, 7):
            actual_day = first_day + timedelta(days=i)
            menu_dates.append(str(actual_day))

        dates_response = []
        for date_index in range(7):
            meals_response = {}
            for meal_type in range(5):
                main_user = MainUser.objects.get(username=request.user)
                user = User.objects.get(user=main_user)
                client = Client.objects.get(user=user)
                try:
                    client_menu = ClientMenu.objects.get(client=client)
                    menu = Menu.objects.get(id=client_menu.menu_id)
                    meals = list(Meal.objects.filter(
                        menu=menu, date=datetime.datetime.strptime(menu_dates[date_index], '%Y-%m-%d').date()))
                    recipe = Recipe.objects.get(
                        id=meals[int(meal_type)].recipe_id)
                    rec_ingredient = RecipeIngredient.objects.filter(
                        recipe=recipe)

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
                    meals_response[recipe.type] = recipe_data
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            dates_response.append(meals_response)
        return Response(dates_response)


class DietGeneratorView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        main_user = MainUser.objects.get(username=request.user)
        user = User.objects.get(user=main_user)
        client = Client.objects.get(user=user)

        preferred_ingredients = []
        try:
            preferred_ingredients_rel = PreferredIngredient.objects.filter(
                client=client)
            for rel in preferred_ingredients_rel:
                preferred_ingredients.append(rel.ingredient)
        except:
            pass

        standard_ingredients = []
        try:
            standard_ingredients_rel = StandardClientIngredient.objects.filter(
                client=client)
            for rel in standard_ingredients_rel:
                standard_ingredients.append(rel.ingredient)
        except:
            pass

        client_allergens = []
        try:
            client_allergens_rel = ClientAllergen.objects.filter(
                client=client)
            for rel in client_allergens_rel:
                client_allergens.append(rel.allergen)
        except:
            pass

        ingredients_allergens = []

        for allergen in client_allergens:
            allergens_query = IngredientAllergen.objects.filter(
                allergen=allergen)
            for a in allergens_query:
                ingredients_allergens.append(a)

        ingredients_to_remove = []
        for i_a in ingredients_allergens:
            ingredients_to_remove.append(i_a.ingredient)

        recipe_ingredients_to_remove = []
        for recipe_ingredient_to_remove in ingredients_to_remove:
            r_i = RecipeIngredient.objects.filter(
                ingredient=recipe_ingredient_to_remove)
            for i in r_i:
                recipe_ingredients_to_remove.append(i)

        recipes_to_remove = []
        for iterator in recipe_ingredients_to_remove:
            recipes_to_remove.append(iterator.recipe.name)

        recipes_without_allergens = Recipe.objects.exclude(
            name__in=recipes_to_remove)

        menu_dates = []

        actual_day = datetime.date.today()
        first_day = actual_day
        index = 0
        while not first_day.weekday() == 0:
            index = index + 1
            first_day = actual_day - timedelta(days=index)

        menu_dates_test = []
        actual_day = first_day
        for i in range(0, 7):
            actual_day = first_day + timedelta(days=i)
            converted_date = map(lambda element: int(
                element), str(actual_day).split('-'))
            menu_dates.append(list(converted_date))

        meal_types = [
            'sniadanie',
            'II sniadanie',
            'obiad',
            'podwieczorek',
            'kolacja'
        ]

        try:
            old_client_menu = ClientMenu.objects.get(client=client)
            old_menu = Menu.objects.filter(clientmenu=old_client_menu)
            for iterator in old_menu:
                old_meals = Meal.objects.filter(menu=iterator).delete()
            old_client_menu.delete()
            old_menu = Menu.objects.filter(clientmenu=old_client_menu).delete()
        except:
            pass

        new_menu = Menu(date_from=datetime.date(2020, 11, 16),
                        date_to=datetime.date(2020, 11, 22), calories=1000)
        new_menu.save()

        new_client_menu = ClientMenu(client=client, menu=new_menu)
        new_client_menu.save()

        for meal_type in meal_types:

            breakfasts = recipes_without_allergens.filter(type=meal_type)
            breakfasts_priorities = []
            for breakfast in breakfasts:
                breakfast_recipe_ingredients = RecipeIngredient.objects.filter(
                    recipe=breakfast)
                breakfast_ingredients = []
                for iterator in breakfast_recipe_ingredients:
                    if not iterator.ingredient in breakfast_ingredients:
                        breakfast_ingredients.append(iterator.ingredient)
                preferred_ingredients_count = 5
                for breakfast_ingredient in breakfast_ingredients:
                    if breakfast_ingredient in preferred_ingredients:
                        preferred_ingredients_count += 30
                    if breakfast_ingredient in standard_ingredients:
                        preferred_ingredients_count += 5
                breakfasts_priorities.append(preferred_ingredients_count)

            total_probability = 0
            distribution = []
            iterator = 0
            for priority in breakfasts_priorities:
                total_probability += priority
                for i in range(priority):
                    distribution.append(iterator)
                iterator += 1
            random.shuffle(distribution, random.random)

            for date in menu_dates:

                new_recipe = breakfasts[random.choice(distribution)]

                new_meal = Meal(menu=new_menu, recipe=new_recipe, calories=300,
                                date=datetime.date(date[0], date[1], date[2]))
                new_meal.save()

        return Response(status=status.HTTP_200_OK)


class ClientDataGetView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        main_user = MainUser.objects.get(username=request.user)
        user = User.objects.get(user=main_user)
        client = Client.objects.get(user=user)

        preferred_ingredients = []
        try:
            preferred_ingredients_rel = PreferredIngredient.objects.filter(
                client=client)
            for rel in preferred_ingredients_rel:
                preferred_ingredients.append(rel.ingredient.name)
        except:
            pass

        standard_ingredients = []
        try:
            standard_ingredients_rel = StandardClientIngredient.objects.filter(
                client=client)
            for rel in standard_ingredients_rel:
                standard_ingredients.append(rel.ingredient.name)
        except:
            pass

        client_allergens = []
        try:
            client_allergens_rel = ClientAllergen.objects.filter(
                client=client)
            for rel in client_allergens_rel:
                client_allergens.append(rel.allergen.name)
        except:
            pass

        response = {
            'login': main_user.username,
            'email': main_user.email,
            'name': client.name,
            'last_name': client.last_name,
            'weight': client.weight,
            'height': client.height,
            'age': client.age,
            'gender': client.gender,
            'physical_activity': client.physical_activity,
            'preferred_ingredients': preferred_ingredients,
            'standard_ingredients': standard_ingredients,
            'client_allergens': client_allergens,
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
        gender = serializer.data.get('gender')
        physical_activity = serializer.data.get('physical_activity')
        serialized_preferred_ingredients = serializer.data.get(
            'preferred_ingredients')
        serialized_standard_ingredients = serializer.data.get(
            'standard_ingredients')
        serialized_allergens = serializer.data.get('allergens')

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
            client.gender = gender
            client.physical_activity = physical_activity
            
            main_user.save()
            client.save()

            PreferredIngredient.objects.all().delete()
            for ingredient in serialized_preferred_ingredients:
                try:
                    preferred_ingredient = Ingredient.objects.get(
                        name=ingredient)
                    preferred_ingredients_save = PreferredIngredient(
                        client=client, ingredient=preferred_ingredient)
                    preferred_ingredients_save.save()
                except:
                    pass

            StandardClientIngredient.objects.all().delete()
            for ingredient in serialized_standard_ingredients:
                try:
                    standard_ingredient = Ingredient.objects.get(
                        name=ingredient)
                    standard_ingredient_save = StandardClientIngredient(
                        client=client, ingredient=standard_ingredient)
                    standard_ingredient_save.save()
                except:
                    pass

            ClientAllergen.objects.all().delete()
            for allergen in serialized_allergens:
                try:
                    allergen = Allergen.objects.get(name=allergen)
                    allergen_save = ClientAllergen(
                        client=client, allergen=allergen)
                    allergen_save.save()
                except:
                    pass

            return Response(status=status.HTTP_200_OK)


class FileDownloader(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, file):
        try:
            meals_folder = os.path.join(settings.IMAGES_DIR, "Dania")
            results_folder = os.path.join(meals_folder, file)
            return FileResponse(open(results_folder, 'rb'))
        except FileNotFoundError:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RecipesView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        recipes = Recipe.objects.all()
        return_recipes = []
        for recipe in recipes:
            rec_ingredient = RecipeIngredient.objects.filter(recipe=recipe)
            ingredients = []
            for i in rec_ingredient:
                ingredients.append(i.ingredient.name)
            recipe_data = {
                'name': recipe.name,
                'method': recipe.method,
                'type': recipe.type,
                'calories': recipe.calories,
                'ingredients': ingredients,
            }
            return_recipes.append(recipe_data)
        return Response(return_recipes)


class IngredientsView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        ingredients = Ingredient.objects.all()
        ingredients_names = []
        for ingredient in ingredients:
            ingredients_names.append(ingredient.name)
        return Response(ingredients_names)


class AllergensView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        allergens = Allergen.objects.all()
        allergens_names = []
        for allergen in allergens:
            allergens_names.append(allergen.name)
        return Response(allergens_names)
