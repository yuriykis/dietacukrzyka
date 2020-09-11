from django.db import models
import datetime

class User(models.Model):
    login = models.CharField("Login", default = "", max_length = 50, null = False)
    password = models.CharField("Password", default = "", max_length = 255, null = False)
    isDietician = models.BooleanField("IsDietician", default = False)
    isAdmin = models.BooleanField("IsAdmin", default = False)

    def __str__(self):
        return self.login

class Dietician(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        primary_key=True
    )
    name = models.CharField("Name", default = "", max_length = 255, null = False)
    last_name = models.CharField("Last Name", default = "", max_length = 255, null = False)

    def __str__(self):
        return self.name + self.last_name

class Client(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        primary_key=True
    )
    name = models.CharField("Name", default = "", max_length = 255, null = False)
    last_name = models.CharField("Last Name", default = "", max_length = 255, null = False)
    weight = models.DecimalField("Weight", max_digits=6, decimal_places=3, default = 0, null = False)
    height = models.DecimalField("Height", max_digits=6, decimal_places=3, default = 0, null = False)
    age = models.IntegerField("Age", default = 0, null = False) 
    
    def __str__(self):
        return self.name + self.last_name

class Disease(models.Model):
    name = models.CharField("Name", default = "", max_length = 255, null = False)

    def __str__(self):
        return self.name


class UserDisease(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.user + self.disease

class Ingredient(models.Model):
    name = models.CharField("Name", default = "", max_length = 255, null = False)
    calories = models.IntegerField("Calories", default = 0, null = False)
    proteins = models.DecimalField("Proteins", max_digits=6, decimal_places=3, default = 0, null = False)
    fats = models.DecimalField("Fats", max_digits=6, decimal_places=3, default = 0, null = False) 
    carbs = models.DecimalField("Carbs", max_digits=6, decimal_places=3, default = 0, null = False) 
    
    def __str__(self):
        return self.name

class PreferredIngredient(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
        )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.ingredient + self.allergen


class Allergen(models.Model):
    name = models.CharField("Name", default = "", max_length = 255, null = False)

    def __str__(self):
        return self.name

class IngredientAllergen(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
        )
    allergen = models.ForeignKey(
        Allergen,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.ingredient + self.allergen

class Recipe(models.Model):
    name = models.CharField("Name", default = "", max_length = 255, null = False)
    method = models.TextField("Method", default = "", null = False)
    calories = models.IntegerField("Calories", default = 0, null = False)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
        )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
        )

    weight = models.DecimalField("Weight", max_digits=6, decimal_places=3, default = 0, null = False)
    
    def __str__(self):
        return self.ingredient + self.recipe

class Menu(models.Model):
    date_from = models.DateField("Name", default=datetime.date.today, null = False)
    date_to= models.DateField("Name", default=datetime.date.today, null = False)
    calories = models.IntegerField("Calories", default = 0, null = False)

    def __str__(self):
        return str(self.date_from)

class MenuRecipe(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE
        )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
        )

    date = models.DateField("Name", default=datetime.date.today, null = False)
    
    def __str__(self):
        return self.menu + self.recipe