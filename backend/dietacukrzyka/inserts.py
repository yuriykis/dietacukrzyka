from zdrowadieta.models import *
import datetime 

user = MainUser.objects.create_user(username = 'jKowalski', password = 'Kowalski123')
new_user1 = User(user = user, isAdmin = True, isDietician = False)
new_user1.save()

new_client1 = Client(user = new_user1, name = 'Kajetan', last_name = 'Kwiatkowski', weight = 85, height = 175, age = 44)
new_client1.save()


user = MainUser.objects.create_user(username = 'mZalewski', password = 'Zalewski123')
new_user2 = User(user = user, isAdmin = False, isDietician = True)
new_user2.save()

new_dietician1 = Dietician(user = new_user2, name = 'Mateusz', last_name = 'Zalewski')
new_dietician1.save()


user = MainUser.objects.create_user(username = 'kKaczmarczyk', password = 'Kaczmarczyk123')
new_user3 = User(user = user, isAdmin = False, isDietician = False)
new_user3.save()

new_client2 = Client(user = new_user3, name = 'Kamil', last_name = 'Kaczmarczyk', weight = 105, height = 172, age = 59)
new_client2.save()


new_disease1 = Disease(name = 'Cukrzyca typu 1')
new_disease1.save()
new_disease2 = Disease(name = 'Cukrzyca typu 2')
new_disease2.save()


new_user_disease = UserDisease(user = new_user1, disease = new_disease1)
new_user_disease.save()
new_user_disease = UserDisease(user = new_user2, disease = new_disease2)
new_user_disease.save()
new_user_disease = UserDisease(user = new_user3, disease = new_disease1)
new_user_disease.save()


new_ingredient = Ingredient(name = 'Ser żółty', calories = 225, proteins= 24.9, fats = 27.4, carbs = 2.22)
new_ingredient.save()
new_ingredient = Ingredient(name = 'Ogórek', calories = 56, proteins= 5.73, fats = 27.4, carbs = 2.22)
new_ingredient.save()
new_ingredient = Ingredient(name = 'Kurczak', calories = 158, proteins= 18.6, fats = 9.3, carbs = 0.0)
new_ingredient.save()
new_ingredient = Ingredient(name = 'Kalafior', calories = 25, proteins= 1.92, fats = 0.28, carbs = 4.97)
new_ingredient.save()
new_ingredient = Ingredient(name = 'Łosoś', calories = 18.4, proteins= 7.5, fats = 27.4, carbs = 4.5)
new_ingredient.save()

new_allergen = Allergen(name = 'Gluten')
new_allergen.save()
new_allergen = Allergen(name = 'Jaja')
new_allergen.save()

new_recipe1 = Recipe(name = 'Owsianka z pomarańczą', method = 'Płatki owsiane zalać wrzątkiem i przykryć talerzykiem. Po chwili dodać jogurt, orzechy i pokrojoną pomarańcze.', calories = 200, type = 'sniadanie')
new_recipe1.save()
new_recipe2 = Recipe(name = 'Owsianka z pomarańczą', method = 'Płatki owsiane zalać wrzątkiem i przykryć talerzykiem. Po chwili dodać jogurt, orzechy i pokrojoną pomarańcze.', calories = 200, type = 'II sniadanie')
new_recipe2.save()
new_recipe3 = Recipe(name = 'Jajecznica na maśle', method = 'Rozpuścić masło na patelni, wbić jaja i wymieszać. Podawać z pieczywem i pokrojonym pomidorem.', calories = 250, type = 'obiad')
new_recipe3.save()
new_recipe4 = Recipe(name = 'Serek wiejski z pomidorem i szczypiorkiem', method = 'Do serka wiejskiego dodać drobno pokrojonego pomidora oraz szczypiorek. Doprawić solą i pieprzem do smaku.', calories = 200, type = 'podwieczorek')
new_recipe4.save()
new_recipe5 = Recipe(name = 'Łosoś pieczony', method = 'Rybę doprawić solą i pieprzem. Wstawić do nagrzanego do 180 stopni piekarnika i piec przez 25 minut. Fasolkę szparagową gotować w osolonej wodzie 12 minut. Podawać z pokrojonym pomidorem.', calories = 300, type = 'kolacja')
new_recipe5.save()

new_menu = Menu(date_from = datetime.date(2020, 10, 12), date_to = datetime.date(2020, 10, 19), calories = 1000)
new_menu.save()

new_client_menu = ClientMenu(client = new_client1, menu = new_menu)
new_client_menu.save()

new_meal1 = Meal(menu = new_menu, recipe = new_recipe1, calories = 200, date = datetime.date(2020, 10, 12))
new_meal1.save()
new_meal2 = Meal(menu = new_menu, recipe = new_recipe2, calories = 250, date = datetime.date(2020, 10, 12))
new_meal2.save()
new_meal3 = Meal(menu = new_menu, recipe = new_recipe3, calories = 250, date = datetime.date(2020, 10, 12))
new_meal3.save()
new_meal4 = Meal(menu = new_menu, recipe = new_recipe4, calories = 200, date = datetime.date(2020, 10, 12))
new_meal4.save()
new_meal5 = Meal(menu = new_menu, recipe = new_recipe5, calories = 350, date = datetime.date(2020, 10, 12))
new_meal5.save()