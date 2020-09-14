INSERT INTO public.zdrowadieta_user(
	id, "isAdmin", "isDietician", login, password)
	VALUES (1, True, False, 'jKowalski', 'Kowalski123');
INSERT INTO public.zdrowadieta_user(
	id, "isAdmin", "isDietician", login, password)
	VALUES (2, False, True, 'mZalewski', 'Zalewski123');
INSERT INTO public.zdrowadieta_user(
	id, "isAdmin", "isDietician", login, password)
	VALUES (3, False, False, 'kKwiatkowski', 'Kwiatkowski123');
INSERT INTO public.zdrowadieta_user(
	id, "isAdmin", "isDietician", login, password)
	VALUES (4, False, False, 'kKaczmarczyk', 'Kaczmarczyk123');
INSERT INTO public.zdrowadieta_user(
	id, "isAdmin", "isDietician", login, password)
	VALUES (5, False, False, 'oJakubowski', 'Jakubowski123');
INSERT INTO public.zdrowadieta_user(
	id, "isAdmin", "isDietician", login, password)
	VALUES (6, False, False, 'aTomaszewska', 'Tomaszewska123');
INSERT INTO public.zdrowadieta_user(
	id, "isAdmin", "isDietician", login, password)
	VALUES (7, False, False, 'aJankowska', 'Jankowska123');

INSERT INTO public.zdrowadieta_dietician(
	user_id, name, last_name)
	VALUES (2, 'Mateusz', 'Zalewski');

INSERT INTO public.zdrowadieta_client(
	user_id, name, last_name, weight, height, age)
	VALUES (3, 'Kajetan', 'Kwiatkowski', 85, 175, 44);
INSERT INTO public.zdrowadieta_client(
	user_id, name, last_name, weight, height, age)
    VALUES (4, 'Kamil', 'Kaczmarczyk', 105, 172, 59);
INSERT INTO public.zdrowadieta_client(
	user_id, name, last_name, weight, height, age)
	VALUES (5, 'Oskar', 'Jakubowski', 98, 177, 62);
INSERT INTO public.zdrowadieta_client(
	user_id, name, last_name, weight, height, age)
	VALUES (6, 'Agnieszka', 'Tomaszewska', 84, 166, 57);
INSERT INTO public.zdrowadieta_client(
	user_id, name, last_name, weight, height, age)
	VALUES (7, 'Anna', 'Jankowska', 77, 162, 68);

INSERT INTO public.zdrowadieta_disease(
	id, name)
	VALUES (1, 'Cukrzyca typu 1');
INSERT INTO public.zdrowadieta_disease(
	id, name)
	VALUES (2, 'Cukrzyca typu 2');

INSERT INTO public.zdrowadieta_userdisease(
	id, disease_id, user_id)
	VALUES (1, 2, 3);
INSERT INTO public.zdrowadieta_userdisease(
	id, disease_id, user_id)
	VALUES (2, 1, 4);
INSERT INTO public.zdrowadieta_userdisease(
	id, disease_id, user_id)
	VALUES (3, 2, 5);
INSERT INTO public.zdrowadieta_userdisease(
	id, disease_id, user_id)
	VALUES (4, 2, 6);
INSERT INTO public.zdrowadieta_userdisease(
	id, disease_id, user_id)
	VALUES (5, 2, 7);


INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (1, 'Platki owsiane', 366, 13.15, 6.52, 67.7);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (2, 'Jogurt naturalny', 56, 5.73, 0.18, 7.68);	
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (3, 'Pomarańcz', 47, 0.94, 0.12, 11.75);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (4, 'Orzechy nerkowca', 533, 18.22, 43.85, 30.19);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (5, 'Jajka', 155, 12.58, 10.61, 1.12);

INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (6, 'Pieczywo żytnie', 225, 6.8, 1.8, 44.7);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (7, 'Masło', 744, 0.63, 82.38, 0.7);	
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (8, 'Wędlina drobiowa', 126, 17.89, 4.98, 1.43);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (9, 'Pomidor', 18, 0.88, 0.2, 3.89);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (10, 'Sałata', 14, 0.9, 0.14, 2.97);

INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (11, 'Ser żółty', 225, 24.9, 27.4, 2.22);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (12, 'Ogórek', 56, 5.73, 0.18, 7.68);	
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (13, 'Kurczak', 158, 18.6, 9.3, 0.0);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (14, 'Kalafior', 25, 1.92, 0.28, 4.97);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (15, 'Łosoś', 159, 18.4, 7.5, 4.5);

INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (16, 'Brokuł', 34, 2.82, 0.37, 6.64);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (17, 'Fasolka szparagowa', 345, 22.0, 2.6, 60.7);	
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (18, 'Marchew', 36, 0.78, 0.46, 7.9);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (19, 'Orzechy włoskie', 654, 15.23, 65.2, 13.71);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (20, 'Jabłko', 52, 0.26, 0.17, 13.81);

INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (21, 'Serek wiejski', 97, 11.0, 5.0, 2.0);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (22, 'Szczypiorek', 27, 0.97, 0.47, 5.74);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (23, 'Szpinak', 469, 20.3, 7.7, 83.9);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (24, 'Awokado', 168, 2.0, 15.0, 4.0);
INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (25, 'Słonecznik', 584, 20.78, 51.46, 20.0);

INSERT INTO public.zdrowadieta_ingredient(
	id, name, calories, proteins, fats, carbs)
	VALUES (26, 'Oliwa z oliwek', 884, 0.0, 100.0, 0.0);


INSERT INTO public.zdrowadieta_allergen(
	id, name)
	VALUES (1, 'Gluten');
INSERT INTO public.zdrowadieta_allergen(
	id, name)
	VALUES (2, 'Jaja');
INSERT INTO public.zdrowadieta_allergen(
	id, name)
	VALUES (3, 'Ryby');
INSERT INTO public.zdrowadieta_allergen(
	id, name)
	VALUES (4, 'Orzechy');


INSERT INTO public.zdrowadieta_ingredientallergen(
	id, allergen_id, ingredient_id)
	VALUES (1, 1, 1);
INSERT INTO public.zdrowadieta_ingredientallergen(
	id, allergen_id, ingredient_id)
	VALUES (2, 4, 4);
INSERT INTO public.zdrowadieta_ingredientallergen(
	id, allergen_id, ingredient_id)
	VALUES (3, 1, 6);
INSERT INTO public.zdrowadieta_ingredientallergen(
	id, allergen_id, ingredient_id)
	VALUES (4, 3, 15);
INSERT INTO public.zdrowadieta_ingredientallergen(
	id, allergen_id, ingredient_id)
	VALUES (5, 2, 5);
INSERT INTO public.zdrowadieta_ingredientallergen(
	id, allergen_id, ingredient_id)
	VALUES (6, 4, 19);

INSERT INTO public.zdrowadieta_recipe(
	id, name, method, calories)
	VALUES (1, 'Owsianka z pomarańczą', 'Płatki owsiane zalać wrzątkiem i przykryć talerzykiem. Po chwili dodać jogurt, orzechy i pokrojoną pomarańcze.', 100);
INSERT INTO public.zdrowadieta_recipe(
	id, name, method, calories)
	VALUES (2, 'Jajecznica na maśle', 'Rozpuścić masło na patelni, wbić jaja i wymieszać. Podawać z pieczywem i pokrojonym pomidorem.', 150);
INSERT INTO public.zdrowadieta_recipe(
	id, name, method, calories)
	VALUES (3, 'Serek wiejski z pomidorem i szczypiorkiem', 'Do serka wiejskiego dodać drobno pokrojonego pomidora oraz szczypiorek. Doprawić solą i pieprzem do smaku.', 100);
INSERT INTO public.zdrowadieta_recipe(
	id, name, method, calories)
	VALUES (4, 'Łosoś pieczony', 'Rybę doprawić solą i pieprzem. Wstawić do nagrzanego do 180 stopni piekarnika i piec przez 25 minut. Fasolkę szparagową gotować w osolonej wodzie 12 minut. Podawać z pokrojonym pomidorem.', '200');


INSERT INTO public.zdrowadieta_menu(
	id, date_from, date_to, calories)
	VALUES (1, '12/10/2020', '19/10/2020', 1000);

INSERT INTO public.zdrowadieta_menurecipe(
	id, date, menu_id, recipe_id)
	VALUES (1, '12/10/2020', 1, 1);
INSERT INTO public.zdrowadieta_menurecipe(
	id, date, menu_id, recipe_id)
	VALUES (2, '12/10/2020', 1, 2);
INSERT INTO public.zdrowadieta_menurecipe(
	id, date, menu_id, recipe_id)
	VALUES (3, '12/10/2020', 1, 3);
INSERT INTO public.zdrowadieta_menurecipe(
	id, date, menu_id, recipe_id)
	VALUES (4, '12/10/2020', 1, 4);

