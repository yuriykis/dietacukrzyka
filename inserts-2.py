from zdrowadieta.models import *
import datetime

user = MainUser.objects.create_user(
    username='jKowalski', password='Kowalski123')
new_user1 = User(user=user, isAdmin=True, isDietician=False)
new_user1.save()
new_client1 = Client(user=new_user1, name='Jan',
                     last_name='Kowalski', weight=85, height=175, age=44)
new_client1.save()


user = MainUser.objects.create_user(
    username='mZalewski', password='Zalewski123')
new_user2 = User(user=user, isAdmin=False, isDietician=True)
new_user2.save()
new_dietician1 = Dietician(
    user=new_user2, name='Mateusz', last_name='Zalewski')
new_dietician1.save()


user = MainUser.objects.create_user(
    username='kKaczmarczyk', password='Kaczmarczyk123')
new_user3 = User(user=user, isAdmin=False, isDietician=False)
new_user3.save()
new_client2 = Client(user=new_user3, name='Kamil',
                     last_name='Kaczmarczyk', weight=105, height=172, age=59)
new_client2.save()


new_disease1 = Disease(name='Cukrzyca typu 1')
new_disease1.save()
new_disease2 = Disease(name='Cukrzyca typu 2')
new_disease2.save()


new_user_disease = UserDisease(user=new_user1, disease=new_disease1)
new_user_disease.save()
new_user_disease = UserDisease(user=new_user2, disease=new_disease2)
new_user_disease.save()
new_user_disease = UserDisease(user=new_user3, disease=new_disease1)
new_user_disease.save()
new_user_disease = UserDisease(user=new_user2, disease=new_disease2)
new_user_disease.save()
new_user_disease = UserDisease(user=new_user2, disease=new_disease2)
new_user_disease.save()
new_user_disease = UserDisease(user=new_user2, disease=new_disease2)
new_user_disease.save()


######
ser = Ingredient(name='Ser żółty', calories=225,
                 proteins=24.9, fats=27.4, carbs=2.22)
ser.save()
ogorek = Ingredient(name='Ogórek', calories=56,
                    proteins=5.73, fats=0.18, carbs=7.68)
ogorek.save()
kurczak = Ingredient(name='Kurczak', calories=158,
                     proteins=18.6, fats=9.3, carbs=0.0)
kurczak.save()
kalafior = Ingredient(name='Kalafior', calories=25,
                      proteins=1.92, fats=0.28, carbs=4.97)
kalafior.save()
losos = Ingredient(name='Łosoś', calories=159,
                   proteins=18.4, fats=7.5, carbs=4.5)
losos.save()
platkiO = Ingredient(name='Platki owsiane', calories=366,
                     proteins=13.15, fats=6.52, carbs=67.7)
platkiO.save()
jogurt = Ingredient(name='Jogurt naturalny', calories=56,
                    proteins=5.73, fats=0.18, carbs=7.68)
jogurt.save()
pomarancza = Ingredient(name='Pomarańcza', calories=47,
                        proteins=0.94, fats=0.12, carbs=11.75)
pomarancza.save()
orzechyN = Ingredient(name='Orzechy nerkowca', calories=533,
                      proteins=18.22, fats=43.85, carbs=30.19)
orzechyN.save()
pieczywo = Ingredient(name='Pieczywo żytnie', calories=225,
                      proteins=6.8, fats=1.8, carbs=44.7)
pieczywo.save()
maslo = Ingredient(name='Masło', calories=744,
                   proteins=0.63, fats=82.38, carbs=0.7)
maslo.save()
szynka = Ingredient(name='Wędlina drobiowa', calories=126,
                    proteins=17.89, fats=4.98, carbs=1.43)
szynka.save()
pomidor = Ingredient(name='Pomidor', calories=18,
                     proteins=0.88, fats=0.2, carbs=3.89)
pomidor.save()
salata = Ingredient(name='Sałata', calories=14,
                    proteins=0.9, fats=0.14, carbs=2.97)
salata.save()
brokul = Ingredient(name='Brokuł', calories=34,
                    proteins=2.82, fats=0.37, carbs=6.64)
brokul.save()
fasolkaS = Ingredient(name='Fasolka szparagowa',
                      calories=345, proteins=22.0, fats=2.6, carbs=60.7)
fasolkaS.save()
marchew = Ingredient(name='Marchew', calories=36,
                     proteins=0.78, fats=0.46, carbs=7.9)
marchew.save()
orzechyW = Ingredient(name='Orzechy włoskie', calories=654,
                      proteins=15.23, fats=65.2, carbs=13.71)
orzechyW.save()
jablko = Ingredient(name='Jabłko', calories=52,
                    proteins=0.26, fats=0.17, carbs=13.81)
jablko.save()
serekW = Ingredient(name='Serek wiejski', calories=97,
                    proteins=11.0, fats=5.0, carbs=2.0)
serekW.save()
szczypior = Ingredient(name='Szczypiorek', calories=27,
                       proteins=0.97, fats=0.47, carbs=5.74)
szczypior.save()
szpinak = Ingredient(name='Szpinak', calories=469,
                     proteins=20.3, fats=7.7, carbs=83.9)
szpinak.save()
awokado = Ingredient(name='Awokado', calories=168,
                     proteins=2.0, fats=15.0, carbs=4.0)
awokado.save()
slonecznik = Ingredient(name='Słonecznik', calories=584,
                        proteins=20.78, fats=51.46, carbs=20.0)
slonecznik.save()
oliwa = Ingredient(name='Oliwa z oliwek', calories=884,
                   proteins=0.0, fats=100.0, carbs=0.0)
oliwa.save()
jajka = Ingredient(name='Jajka', calories=155,
                   proteins=12.58, fats=10.6, carbs=1.12)
jajka.save()
migdaly = Ingredient(name='Migdały', calories=580,
                     proteins=21.3, fats=50.6, carbs=21.55)
migdaly.save()
mlekoMigdalowe = Ingredient(name='Mleko migdałowe',
                            calories=24, proteins=0.5, fats=1.1, carbs=1.4)
mlekoMigdalowe.save()
borowki = Ingredient(name='Borówki amerykańskie', calories=57,
                     proteins=0.74, fats=0.33, carbs=14.49)
borowki.save()
truskawki = Ingredient(name='Truskawki', calories=32,
                       proteins=0.67, fats=0.30, carbs=7.68)
truskawki.save()
jagody = Ingredient(name='Jagody', calories=57,
                    proteins=0.0, fats=0.14, carbs=13.85)
jagody.save()
banan = Ingredient(name='Banan', calories=97,
                   proteins=1.0, fats=0.3, carbs=21.8)
banan.save()
maliny = Ingredient(name='Maliny', calories=52,
                    proteins=1.20, fats=0.65, carbs=11.94)
maliny.save()
siemieLniane = Ingredient(name='Siemię lniane',
                          calories=534, proteins=18.58, fats=42.16, carbs=28.8)
siemieLniane.save()
mleko = Ingredient(name='Mleko 2%', calories=51,
                   proteins=3.3, fats=2.0, carbs=4.9)
mleko.save()
cukinia = Ingredient(name='Cukinia', calories=17,
                     proteins=1.21, fats=0.32, carbs=3.11)
cukinia.save()
papryka = Ingredient(name='Papryka', calories=32,
                     proteins=1.74, fats=0.44, carbs=4.06)
papryka.save()
cebula = Ingredient(name='Cebula', calories=30,
                    proteins=1.4, fats=0.4, carbs=6.9)
cebula.save()
kaszaGryczana = Ingredient(name='Kasza gryczana biała',
                           calories=336, proteins=12.6, fats=3.1, carbs=69.3)
kaszaGryczana.save()
rzodkiewka = Ingredient(name='Rzodkiewka', calories=14,
                        proteins=1.0, fats=0.2, carbs=4.4)
rzodkiewka.save()
suszonePomidory = Ingredient(
    name='Suszone pomidory', calories=215, proteins=5.0, fats=14.0, carbs=23.0)
suszonePomidory.save()
tilapia = Ingredient(name='Tilapia', calories=90,
                     proteins=13.0, fats=4.0, carbs=0.0)
tilapia.save()
tunczyk = Ingredient(name='Tuńczyk', calories=132,
                     proteins=28.0, fats=1.0, carbs=0.0)
tunczyk.save()
szparagi = Ingredient(name='Szparagi', calories=18,
                      proteins=1.9, fats=0.2, carbs=3.7)
szparagi.save()
masloOrzechowe = Ingredient(name='Masło orzechowe',
                            calories=634, proteins=26.6, fats=53.0, carbs=8.5)
masloOrzechowe.save()
hummus = Ingredient(name='Hummus z ciecierzycy', calories=177,
                    proteins=4.86, fats=8.6, carbs=20.12)
hummus.save()
feta = Ingredient(name='Ser feta', calories=215,
                  proteins=17.0, fats=16.0, carbs=1.0)
feta.save()
jarmuz = Ingredient(name='Jarmuż', calories=29,
                    proteins=3.3, fats=0.7, carbs=6.1)
jarmuz.save()
czosnek = Ingredient(name='Czosnek', calories=146,
                     proteins=6.4, fats=0.5, carbs=32.6)
czosnek.save()
mozzarella = Ingredient(name='Mozzarella', calories=254,
                        proteins=24.0, fats=16.0, carbs=3.0)
mozzarella.save()
lososWedzony = Ingredient(name='Łosoś wędzony',
                          calories=162, proteins=21.5, fats=8.4, carbs=0.0)
lososWedzony.save()
otreby = Ingredient(name='Otręby przenne', calories=185,
                    proteins=16.0, fats=4.6, carbs=61.9)
otreby.save()
baklazan = Ingredient(name='Bakłażan', calories=25,
                      proteins=1.0, fats=0.18, carbs=5.88)
baklazan.save()
rukola = Ingredient(name='Rukola', calories=25,
                    proteins=2.6, fats=0.7, carbs=3.7)
rukola.save()
groszekZielony = Ingredient(name='Groszek zielony',
                            calories=76, proteins=6.7, fats=0.4, carbs=17.0)
groszekZielony.save()
krewetki = Ingredient(name='Krewetki', calories=71,
                      proteins=13.6, fats=1.0, carbs=0.0)
krewetki.save()
ciecierzyca = Ingredient(name='Ciecierzyca', calories=163,
                         proteins=8.86, fats=2.59, carbs=27.42)
ciecierzyca.save()
pomidoryZPuszki = Ingredient(
    name='Pomidory z puszki', calories=32, proteins=1.64, fats=0.28, carbs=8.9)
pomidoryZPuszki.save()
oliwki = Ingredient(name='Oliwki zielone', calories=81,
                    proteins=1.0, fats=6.9, carbs=5.6)
oliwki.save()
soczewica = Ingredient(name='Soczewica', calories=116,
                       proteins=9.0, fats=0.4, carbs=20.9)
soczewica.save()
ryz = Ingredient(name='Ryż pełnoziarnisty', calories=385,
                 proteins=7.7, fats=2.2, carbs=75.7)
ryz.save()
gruszka = Ingredient(name='Gruszka', calories=57,
                     proteins=0.36, fats=0.14, carbs=14.9)
gruszka.save()
wisnia = Ingredient(name='Wiśnie', calories=50,
                    proteins=1.0, fats=0.3, carbs=12.2)
wisnia.save()
brzoskwinia = Ingredient(name='Brzoskwinia', calories=39,
                         proteins=0.9, fats=0.25, carbs=9.5)
brzoskwinia.save()
fasolaCzerwona = Ingredient(name='Fasola czerwona',
                            calories=124, proteins=8.0, fats=1.0, carbs=21.5)
fasolaCzerwona.save()
burak = Ingredient(name='Burak', calories=43,
                   proteins=1.6, fats=0.17, carbs=9.6)
burak.save()


gluten_alerg = Allergen(name='Gluten')
gluten_alerg.save()
jaja_alerg = Allergen(name='Jaja')
jaja_alerg.save()
lubin_alerg = Allergen(name='Łubin')
lubin_alerg.save()
mieczaki_alerg = Allergen(name='Mięczaki')
mieczaki_alerg.save()
mleko_alerg = Allergen(name='Mleko')
mleko_alerg.save()
musztarda_alerg = Allergen(name='Musztarda')
musztarda_alerg.save()
orzechy_alerg = Allergen(name='Orzechy')
orzechy_alerg.save()
orzechy_ziemne_alerg = Allergen(name='Orzechy ziemne')
orzechy_ziemne_alerg.save()
ryby_alerg = Allergen(name='Ryby')
ryby_alerg.save()
sezam_alerg = Allergen(name='Sezam')
sezam_alerg.save()
soja_alerg = Allergen(name='Soja')
soja_alerg.save()

ingredient_allergen = IngredientAllergen(
    ingredient=pieczywo, allergen=gluten_alerg)
ingredient_allergen.save()
ingredient_allergen = IngredientAllergen(
    ingredient=platkiO, allergen=gluten_alerg)
ingredient_allergen.save()
ingredient_allergen = IngredientAllergen(
    ingredient=ciecierzyca, allergen=gluten_alerg)
ingredient_allergen.save()
ingredient_allergen = IngredientAllergen(
    ingredient=soczewica, allergen=gluten_alerg)
ingredient_allergen.save()
ingredient_allergen = IngredientAllergen(
    ingredient=jarmuz, allergen=gluten_alerg)
ingredient_allergen.save()
ingredient_allergen = IngredientAllergen(ingredient=ryz, allergen=gluten_alerg)
ingredient_allergen.save()
ingredient_allergen = IngredientAllergen(ingredient=jajka, allergen=jaja_alerg)
ingredient_allergen.save()
ingredient_allergen = IngredientAllergen(
    ingredient=mleko, allergen=mleko_alerg)
ingredient_allergen.save()
ingredient_allergen = IngredientAllergen(
    ingredient=orzechyW, allergen=orzechy_alerg)
ingredient_allergen.save()
ingredient_allergen = IngredientAllergen(
    ingredient=lososWedzony, allergen=ryby_alerg)
ingredient_allergen.save()
ingredient_allergen = IngredientAllergen(ingredient=losos, allergen=ryby_alerg)
ingredient_allergen.save()
ingredient_allergen = IngredientAllergen(
    ingredient=migdaly, allergen=orzechy_alerg)
ingredient_allergen.save()
ingredient_allergen = IngredientAllergen(
    ingredient=mlekoMigdalowe, allergen=orzechy_alerg)
ingredient_allergen.save()

# sniadania
owsiankaPomarancza = Recipe(name='Owsianka z pomarańczą',
                            method='Płatki owsiane zalać wrzątkiem i przykryć talerzykiem. Po chwili dodać jogurt, orzechy i pokrojoną pomarańcze.', calories=200, type='sniadanie')
owsiankaPomarancza.save()
jajecznica = Recipe(name='Jajecznica na maśle',
                    method='Rozpuścić masło na patelni, wbić jaja i wymieszać. Podawać z pieczywem i pokrojonym pomidorem.', calories=250, type='sniadanie')
jajecznica.save()
kanapkaAwokadoJajko = Recipe(name='Kanapka z jajkiem i awokado',
                             method='Jajka gotujemy na twardo przez 8 minut. Podajemy z pieczywem posmarowanym pastą z dojrzałego awokado z dodatkiem przypraw.', calories=200, type='sniadanie')
kanapkaAwokadoJajko.save()
owsiankaOwoce = Recipe(name='Owsianka z owocami i migdałami',
                       method='Płatki owsiane zalać wrzątkiem i przykryć talerzykiem. Po chwili dodać jogurt, borówki, truskawki i migdały.', calories=200, type='sniadanie')
owsiankaOwoce.save()
kanapkaSerekPomidory = Recipe(name='Kanapka z serkiem wiejskim i pomidorkami',
                              method='Na pieczywo położyć serek wiejski, następnie udekorować pomidorkami.', calories=200, type='sniadanie')
kanapkaSerekPomidory.save()
omletJajeczny = Recipe(name='Omlet Jajeczny ', method='Rozbij jajka, rozmieszaj widelcem, dodając odrobinę wody, sól i pieprz. Suchą patelnię postaw na bardzo małym ogniu, potem zwiększ płomień, rozgrzej masło (uważaj, by się nie zrumieniło), wlej masę jajeczną. Smaż bez przykrycia na dużym ogniu, aż brzegi omletu się zetną. Bardzo delikatnie odwróć na drugą stronę, chwilę podsmaż. Podawaj z pomidorami.', calories=200, type='sniadanie')
omletJajeczny.save()
serekOwoce = Recipe(name='Serek wiejski z malinami, jagodami i bananem',
                    method='Serek wiejski wymieszać z owocami. ', calories=200, type='sniadanie')
serekOwoce.save()
jajkaSadzoneSzparagi = Recipe(name='Szparagi z jajkiem sadzonym ',
                              method='Szparagi gotujemy w osolonej wodzie około 7 minut. Jajka rozbijamy na patelnie delikatnie zwilżoną olejem i smażymy pod przykryciem.', calories=200, type='sniadanie')
jajkaSadzoneSzparagi.save()
kanapkaMasloOrzechowe = Recipe(name='Kanapka z masłem orzechowym i bananem',
                               method='Pieczywo posmaruj masłem orzechowym, nasęponie połóż pokrojonego w plastry banana.', calories=200, type='sniadanie')
kanapkaMasloOrzechowe.save()
jajkaSadzoneWarzywa = Recipe(name='Jajka sadzone z warzywami',
                             method='Jajka rozbijamy na patelnie delikatnie zwilżoną olejem i smażymy pod przykryciem. Podajemy z wcześniej pokrojonymi pomidorami, ogórkiem i papryką. Dodatkowo posypujemy świeżym szczypiorkiem.', calories=200, type='sniadanie')
jajkaSadzoneWarzywa.save()
omletOwsianyBanan = Recipe(name='Omlet owsiany z bananem', method='Płatki owsiane zalewamy wodą aby zmiękły. Obranego banana rozgniatamy widelcem. Rozbijamy jajka do miski i mieszamy z bananem i płatkami. Smażymy na małym ogniu pod przykryciem. Podajemy z pokrojonym w plastry bananem.', calories=200, type='sniadanie')
omletOwsianyBanan.save()


# II sniadania
kanapkaSzynkaPomidor = Recipe(
    name='Kanapka z wędliną', method='Bułkę przekroić, posmarować masłem oraz położyć przygotowane składniki.', calories=200, type='II sniadanie')
kanapkaSzynkaPomidor.save()
kanapkaSerOgorek = Recipe(
    name='Kanapka z serem', method='Bułkę przekroić, posmarować masłem oraz położyć przygotowane składniki.', calories=200, type='II sniadanie')
kanapkaSerOgorek.save()
koktajlBananTruskawka = Recipe(name='Koktajl z bananem i truskawkami',
                               method='Do blendera wrzucić umyte owoce, wsypać siemie lniane oraz zalać mlekiem. Blendować do czasu uzyskania jednolitej konsystencji.', calories=200, type='II sniadanie')
koktajlBananTruskawka.save()
koktajlJagoda = Recipe(name='Koktajl jagodowy',
                       method='Do blendera wrzucić umyte jagody, następnie zalać mlekiem migdałowym niesłodzonym. Blendować do czasu uzyskania jednolitej konsystencji.', calories=200, type='II sniadanie')
koktajlJagoda.save()
koktajlTruskawka = Recipe(name='Koktajl truskawkowy',
                          method='Do blendera wrzucić umyte truskawki, dodać jogurt naturalny oraz zalać mlekiem migdałowym niesłodzonym. Blendować do czasu uzyskania jednolitej konsystencji.', calories=200, type='II sniadanie')
koktajlTruskawka.save()
koktajlAwokado = Recipe(name='Koktajl z awokado',
                        method='Do blendera wrzucić banana, awokado oraz zalać mlekiem. Blendować do czasu uzyskania jednolitej konsystencji.', calories=200, type='II sniadanie')
koktajlAwokado.save()
koktajlSzpinak = Recipe(name='Koktajl ze szpinaku',
                        method='Do blendera wrzucić awokado, jabłko oraz szpinak, następnie zalać szklanką wody. Blendować do czasu uzyskania jednolitej konsystencji.', calories=200, type='II sniadanie')
koktajlSzpinak.save()
koktajlMalina = Recipe(name='Koktajl malinowy',
                       method='Do blendera wrzucić umyte maliny, następnie zalać kefirem. Blendować do czasu uzyskania jednolitej konsystencji.', calories=200, type='II sniadanie')
koktajlMalina.save()
ogorekHummus = Recipe(name='Hummus z ogórkiem i marchewką',
                      method='Obrane i pojkrojone marchwki i ogórki podawać z gotowym hummusem z ciecierzycy.', calories=200, type='II sniadanie')
ogorekHummus.save()
koktajlMasloBanan = Recipe(name='Koktajl z masłem orzechowym i bananem',
                           method='Do blendera wrzucić banana, dodać masło orzechowe następnie zalać mlekiem. Blendować do czasu uzyskania jednolitej konsystencji.', calories=200, type='II sniadanie')
koktajlMasloBanan.save()
jogurtBorowkaTruskawka = Recipe(name='Jogurt z borówkami i truskawkami',
                                method='Jogurt naturalny posypać pokrojonymi truskawkami i borówkami.', calories=200, type='II sniadanie')
jogurtBorowkaTruskawka.save()


# Obiady
lososFasolkaPomidor = Recipe(
    name='Łosoś pieczony', method='Rybę doprawić solą i pieprzem. Wstawić do nagrzanego do 180 stopni piekarnika i piec przez 25 minut. Fasolkę szparagową gotować w osolonej wodzie 12 minut. Podawać z pokrojonym pomidorem.', calories=250, type='obiad')
lososFasolkaPomidor.save()
kurczakBrokul = Recipe(name='Kurczak pieczony', method='Mięso doprawić solą oraz suszoną papryką, piec w piekarniku w 190 stopniach przez 1,5 godziny. Umyty i pokrojony brokuł gotować w posolonej wodzie przez 12 minut.', calories=250, type='obiad')
kurczakBrokul.save()
szaszlykLosos = Recipe(name='Szaszłyki z łososiem, cukinią, papryką i cebulą',
                       method='Łososia oraz warzywa pokroić na grubsze kawałki. Na przemian nabić na patyczki. Grillować z obu stron do zrumienienia się ryby i warzyw.', calories=250, type='obiad')
szaszlykLosos.save()
kurczakGrillWarzywa = Recipe(name='Pierś z kurczaka grillowana z warzywami',
                             method='Pierś pokroić na średniej wielkości kawałki i doprawić. Cukinię i paprykę pokroić na większe kawałki. Kurczaka grillować razem z warzywami około 10-15 minut. ', calories=250, type='obiad')
kurczakGrillWarzywa.save()
salatkaJajkoKasza = Recipe(name='Sałatka z jajkiem i kaszą', method='Kaszę ugotować w woreczku, następnie ostudzić. Połączyć z pokrojoną sałatą oraz posiekanym szczypiorkiem i włożyć do szerokiej salaterki. Dodać pokrojone na plasterki rzodkiewki oraz jajka ugotowane na twardo i pokrojone na połówki. Dodać pokrojone na paseczki suszone pomidory.', calories=250, type='obiad')
salatkaJajkoKasza.save()
tilapiaWarzywa = Recipe(name='Grilowana tilapia z cukinią i pomidorami',
                        method='Filety z tilapii umyć, pokroić na kawałki, oprószyć solą. Cukinię, pomidory pokroić na małe kawałki. Rozgrzać ruszt, bądź patelnię do grillowania. Ułożyć rybę , warzywa i grillować około 15 minut.', calories=250, type='obiad')
tilapiaWarzywa.save()
tunczykSzparagi = Recipe(name='Tuńczyk ze szparagami',
                         method='Łososia oraz warzywa pokroić na grubsze kawałki. Na przemian nabić na patyczki. Grillować z obu stron do zrumienienia się ryby i warzyw.', calories=250, type='obiad')
tunczykSzparagi.save()
krewetkiBrokulRyz = Recipe(name='Krewetki ze szpinakiem i ryżem',
                           method='Doprawione solą krewetki podsmażamy na oliwie z posiekanym czosnkiem. Podajemy z ugotowanym brokułem i ryżem. Ryż gotujemy zgodnie z opisem na opakowaniu, natomiast brokuł wrzucamy do osolonej wrzącej wody i gotujemy 6 minut.', calories=250, type='obiad')
krewetkiBrokulRyz.save()
ciecierzycaPomidorySzpinak = Recipe(name='Potrawka z ciecierzycą i szpinakiem',
                                    method='Posiekany w kostkę czosnek podsmażmamy na oliwie. Dodajmy pomidory z puszki, przyprawiamy solą, pieprzem, ziołami prowansalskimi. Na koniec dodajemy gotowaną ciecierzycę i świeży szpinak. Dusimi przez kolejne 5 minut.', calories=250, type='obiad')
ciecierzycaPomidorySzpinak.save()
soczewicaCukinia = Recipe(name='Sałatka z soczewicą i cukinią',
                          method='Soczewicę gotujemy według zaleceń na opakowaniu i ostudzamy. Podsmażamy cukinię. Podajemy z posiekanymi oliwkami i pokruszonym serem feta.', calories=250, type='obiad')
soczewicaCukinia.save()
lososSzpinakRyz = Recipe(name='Łosoś ze szpinakiem i ryżem',
                         method='Rybę doprawić i wstawić do nagrzanego do 180 stopni piekarnika na 20 minut. Ryż ugotować zgodnie z zaleceniami na opakowaniu. Podawać z pokrojonym awokado i świeżym awokado.', calories=250, type='obiad')
lososSzpinakRyz.save()


# Podwieczorki
jablkoOrzechy = Recipe(name='Garść orzechów włoskich, jabłko',
                       method='', calories=200, type='podwieczorek')
jablkoOrzechy.save()
marchewkaPodwieczorek = Recipe(
    name='Surowa marchewka', method='Marchwekę obrać i pokroić.', calories=200, type='podwieczorek')
marchewkaPodwieczorek.save()
jablkoMasloOrzechowe = Recipe(name='Jabłko z masłem orzechowym',
                              method='Umyte jabłka pokroić na średnie kawałki, posmarować masłem orzechowym.', calories=200, type='podwieczorek')
jablkoMasloOrzechowe.save()
orzechyNerkowca = Recipe(name='Garść orzechów nerkowca',
                         method='', calories=200, type='podwieczorek')
orzechyNerkowca.save()
jagodyMigdaly = Recipe(name='Garść migdałów i jagód',
                       method='', calories=200, type='podwieczorek')
jagodyMigdaly.save()
jablkoOrzechy = Recipe(name='Hummus z marchewką',
                       method='Gotowy kupiony hummus podawać z obranymi, pokrojonymi w słupki marchewkami.', calories=200, type='podwieczorek')
jablkoOrzechy.save()
bananPodwieczorek = Recipe(name='Banan', method='',
                           calories=200, type='podwieczorek')
bananPodwieczorek.save()
brzoskwinieWisnie = Recipe(
    name='Brzoskwinia z wiśniami', method='', calories=200, type='podwieczorek')
brzoskwinieWisnie.save()
gruszkaPodwieczorek = Recipe(
    name='Gruszka', method='', calories=200, type='podwieczorek')
gruszkaPodwieczorek.save()
jablkoPodwieczorek = Recipe(
    name='Jabłko', method='', calories=200, type='podwieczorek')
jablkoPodwieczorek.save()
pomaranczPodwieczorek = Recipe(
    name='Pomarańcz', method='', calories=200, type='podwieczorek')
pomaranczPodwieczorek.save()


# Kolacje
serekPomidor = Recipe(name='Serek wiejski z pomidorem i szczypiorkiem',
                      method='* Do serka wiejskiego dodać drobno pokrojonego pomidora oraz szczypiorek. Doprawić solą i pieprzem do smaku.', calories=300, type='kolacja')
serekPomidor.save()
salatkaSzpinak = Recipe(name='Sałatka ze szpinaku',
                        method='Sałatka ze szpinaku, pomidora, awokado, ze słonecznikiem i oliwą.', calories=300, type='kolacja')
salatkaSzpinak.save()
jogurtOtreby = Recipe(name='Jogurt z bananem i otrębami',
                      method='Do jogurtu dodać otręby, następnie wkroić banana.', calories=300, type='kolacja')
jogurtOtreby.save()
kanapkaLosos = Recipe(name='Kanapka z wędzonym łososiem',
                      method='Pieczywo posmarować masłem, następnie ułożyć wędzonego łososia. ', calories=300, type='kolacja')
kanapkaLosos.save()
salatkaCaprese = Recipe(name='Sałatka Caprese',
                        method='Mozzarelle i pomidory pokroić w plastry. Ułożyć naprzemiennie, doprawić solą, pieprzem i bazylią. Podawać z pieczywem żytnim.', calories=300, type='kolacja')
salatkaCaprese.save()
kanapkaAwokadoSzynka = Recipe(name='Kanapki z awokado, szynką drobiową i pomidorami',
                              method='Pieczywo posmaruj rozgniecionym awokado. Na chlebie ułóż plastry szynki i pokrojone pomidory.', calories=300, type='kolacja')
kanapkaAwokadoSzynka.save()
kaszaJarmuz = Recipe(name='Kasza z serem feta, jarmużem i suszonymi pomidorami',
                     method='Kaszę ugotuj według przepisu na opakowaniu. Posiekany czosnek podsmaż na oliwie, następnie dodaj jarmuż i smaż przez 3 minuty ciągle mieszając. Wymieszaj kaszę z warzywami i dodaj pokruszony ser feta. Dopraw pieprzem według uznania. ', calories=300, type='kolacja')
kaszaJarmuz.save()
fasolaKaszaGryczana = Recipe(name='Kasza gryczana z warzywami',
                             method='Kaszę ugotuj według przepisu na opakowaniu. Na talerzu ułóż liście rukoli a na niej pokrojone pomidorki i ugotowane buraki. Podawaj z czerwoną fasolą.', calories=300, type='kolacja')
fasolaKaszaGryczana.save()
salatkaBaklazan = Recipe(name='Sałatka z bakłażanem',
                         method='Pokrojonego bakłażana ugrilować i przestudzić. Do miski włożyć umytą sałatę, pokrojoną mozzarellę oraz pomidory. Na koniec ułożyć kawałki bakłażana.', calories=300, type='kolacja')
salatkaBaklazan.save()
salatkaRukolaFeta = Recipe(name='Sałatka z rukolą i fetą',
                           method='Rukolę umyć i wspypać do miski. Suszone pomidory i ser feta pokroić i dorzucić do miski. Podawać z nasionami słonecznika.', calories=300, type='kolacja')
salatkaRukolaFeta.save()
kurczakSzparagiGroszek = Recipe(name='Grilowana pierś kurczaka ze szparagami i zielonym groszkiem',
                                method='Doprawiony solą filet z piersi kurczka grilować około 12 minut. Podawać z gotowanymi 7 minut szparagami i zielonym groszkiem z puszki.', calories=300, type='kolacja')
kurczakSzparagiGroszek.save()

#############
new_recipeIngredient = RecipeIngredient(
    ingredient=jogurt, recipe=jogurtBorowkaTruskawka, massFraction=0.5)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=borowki, recipe=jogurtBorowkaTruskawka, massFraction=0.25)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=truskawki, recipe=jogurtBorowkaTruskawka, massFraction=0.25)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=masloOrzechowe, recipe=koktajlMasloBanan, massFraction=0.15)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=banan, recipe=koktajlMasloBanan, massFraction=0.25)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=mleko, recipe=koktajlMasloBanan, massFraction=0.6)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=hummus, recipe=ogorekHummus, massFraction=0.5)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=ogorek, recipe=ogorekHummus, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=marchew, recipe=ogorekHummus, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=maliny, recipe=koktajlMalina, massFraction=0.5)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=kefir, recipe=koktajlMalina, massFraction=0.5)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=jajka, recipe=omletOwsianyBanan, massFraction=0.35)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=platkiO, recipe=omletOwsianyBanan, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=banan, recipe=omletOwsianyBanan, massFraction=0.35)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=jajka, recipe=jajkaSadzoneWarzywa, massFraction=0.35)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=papryka, recipe=jajkaSadzoneWarzywa, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=pomidor, recipe=jajkaSadzoneWarzywa, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=ogorek, recipe=jajkaSadzoneWarzywa, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=szczypior, recipe=jajkaSadzoneWarzywa, massFraction=0.05)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=pieczywo, recipe=kanapkaMasloOrzechowe, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=masloOrzechowe, recipe=kanapkaMasloOrzechowe, massFraction=0.25)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=banan, recipe=kanapkaMasloOrzechowe, massFraction=0.35)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=jajka, recipe=jajkaSadzoneSzparagi, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=szparagi, recipe=jajkaSadzoneSzparagi, massFraction=0.6)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=krewetki, recipe=krewetkiBrokulRyz, massFraction=0.25)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=czosnek, recipe=krewetkiBrokulRyz, massFraction=0.05)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=oliwa, recipe=krewetkiBrokulRyz, massFraction=0.05)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=brokul, recipe=krewetkiBrokulRyz, massFraction=0.35)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=ryz, recipe=krewetkiBrokulRyz, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=pomarancza, recipe=pomaranczPodwieczorek, massFraction=1.0)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=jablko, recipe=jablkoPodwieczorek, massFraction=1.0)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=gruszka, recipe=gruszkaPodwieczorek, massFraction=1.0)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=wisnia, recipe=brzoskwinieWisnie, massFraction=0.5)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=brzoskwinia, recipe=brzoskwinieWisnie, massFraction=0.5)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=losos, recipe=lososSzpinakRyz, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=szpinak, recipe=lososSzpinakRyz, massFraction=0.15)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=ryz, recipe=lososSzpinakRyz, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=awokado, recipe=lososSzpinakRyz, massFraction=0.15)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=soczewica, recipe=soczewicaCukinia, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=cukinia, recipe=soczewicaCukinia, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=feta, recipe=soczewicaCukinia, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=oliwki, recipe=soczewicaCukinia, massFraction=0.1)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=czosnek, recipe=ciecierzycaPomidorySzpinak, massFraction=0.05)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=oliwa, recipe=ciecierzycaPomidorySzpinak, massFraction=0.05)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=pomidoryZPuszki, recipe=ciecierzycaPomidorySzpinak, massFraction=0.5)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=ciecierzyca, recipe=ciecierzycaPomidorySzpinak, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=szpinak, recipe=ciecierzycaPomidorySzpinak, massFraction=0.1)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=kurczak, recipe=kurczakSzparagiGroszek, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=szparagi, recipe=kurczakSzparagiGroszek, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=groszekZielony, recipe=kurczakSzparagiGroszek, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=rukola, recipe=salatkaRukolaFeta, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=feta, recipe=salatkaRukolaFeta, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=suszonePomidory, recipe=salatkaRukolaFeta, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=slonecznik, recipe=salatkaRukolaFeta, massFraction=0.1)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=baklazan, recipe=salatkaBaklazan, massFraction=0.25)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=mozzarella, recipe=salatkaBaklazan, massFraction=0.25)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=salata, recipe=salatkaBaklazan, massFraction=0.25)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=pomidor, recipe=salatkaBaklazan, massFraction=0.25)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=kaszaGryczana, recipe=fasolaKaszaGryczana, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=fasolaCzerwona, recipe=fasolaKaszaGryczana, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=burak, recipe=fasolaKaszaGryczana, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=rukola, recipe=fasolaKaszaGryczana, massFraction=0.1)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=pomidor, recipe=fasolaKaszaGryczana, massFraction=0.2)
new_recipeIngredient.save()
#

###
new_recipeIngredient1 = RecipeIngredient(
    ingredient=orzechyN, recipe=owsiankaPomarancza, massFraction=0.1)
new_recipeIngredient1.save()
new_recipeIngredient1 = RecipeIngredient(
    ingredient=pomarancza, recipe=owsiankaPomarancza, massFraction=0.3)
new_recipeIngredient1.save()
new_recipeIngredient2 = RecipeIngredient(
    ingredient=platkiO, recipe=owsiankaPomarancza, massFraction=0.2)
new_recipeIngredient2.save()
new_recipeIngredient3 = RecipeIngredient(
    ingredient=jogurt, recipe=owsiankaPomarancza, massFraction=0.4)
new_recipeIngredient3.save()
new_recipeIngredient4 = RecipeIngredient(
    ingredient=pieczywo, recipe=kanapkaSzynkaPomidor, massFraction=0.2)
new_recipeIngredient4.save()
new_recipeIngredient5 = RecipeIngredient(
    ingredient=maslo, recipe=kanapkaSzynkaPomidor, massFraction=0.2)
new_recipeIngredient5.save()
new_recipeIngredient6 = RecipeIngredient(
    ingredient=szynka, recipe=kanapkaSzynkaPomidor, massFraction=0.2)
new_recipeIngredient6.save()
new_recipeIngredient7 = RecipeIngredient(
    ingredient=pomidor, recipe=kanapkaSzynkaPomidor, massFraction=0.2)
new_recipeIngredient7.save()
new_recipeIngredient8 = RecipeIngredient(
    ingredient=salata, recipe=kanapkaSzynkaPomidor, massFraction=0.4)
new_recipeIngredient8.save()
new_recipeIngredient9 = RecipeIngredient(
    ingredient=losos, recipe=lososFasolkaPomidor, massFraction=0.4)
new_recipeIngredient9.save()
new_recipeIngredient10 = RecipeIngredient(
    ingredient=pomidor, recipe=lososFasolkaPomidor, massFraction=0.4)
new_recipeIngredient10.save()
new_recipeIngredient11 = RecipeIngredient(
    ingredient=fasolkaS, recipe=lososFasolkaPomidor, massFraction=0.2)
new_recipeIngredient11.save()
new_recipeIngredient12 = RecipeIngredient(
    ingredient=marchew, recipe=marchewkaPodwieczorek, massFraction=1.0)
new_recipeIngredient12.save()
new_recipeIngredient13 = RecipeIngredient(
    ingredient=serekW, recipe=serekPomidor, massFraction=0.5)
new_recipeIngredient13.save()
new_recipeIngredient14 = RecipeIngredient(
    ingredient=pomidor, recipe=serekPomidor, massFraction=0.4)
new_recipeIngredient14.save()
new_recipeIngredient15 = RecipeIngredient(
    ingredient=szczypior, recipe=serekPomidor, massFraction=0.1)
new_recipeIngredient15.save()

new_recipeIngredient16 = RecipeIngredient(
    ingredient=pieczywo, recipe=jajecznica, massFraction=0.2)
new_recipeIngredient16.save()
new_recipeIngredient17 = RecipeIngredient(
    ingredient=maslo, recipe=jajecznica, massFraction=0.2)
new_recipeIngredient17.save()
new_recipeIngredient18 = RecipeIngredient(
    ingredient=jajka, recipe=jajecznica, massFraction=0.4)
new_recipeIngredient18.save()
new_recipeIngredient19 = RecipeIngredient(
    ingredient=pomidor, recipe=jajecznica, massFraction=0.2)
new_recipeIngredient19.save()

new_recipeIngredient22 = RecipeIngredient(
    ingredient=maslo, recipe=kanapkaSerOgorek, massFraction=0.2)
new_recipeIngredient22.save()
new_recipeIngredient23 = RecipeIngredient(
    ingredient=ser, recipe=kanapkaSerOgorek, massFraction=0.2)
new_recipeIngredient23.save()
new_recipeIngredient24 = RecipeIngredient(
    ingredient=pieczywo, recipe=kanapkaSerOgorek, massFraction=0.2)
new_recipeIngredient24.save()
new_recipeIngredient25 = RecipeIngredient(
    ingredient=salata, recipe=kanapkaSerOgorek, massFraction=0.2)
new_recipeIngredient25.save()
new_recipeIngredient25 = RecipeIngredient(
    ingredient=ogorek, recipe=kanapkaSerOgorek, massFraction=0.2)
new_recipeIngredient25.save()

new_recipeIngredient26 = RecipeIngredient(
    ingredient=kurczak, recipe=kurczakBrokul, massFraction=0.5)
new_recipeIngredient26.save()
new_recipeIngredient27 = RecipeIngredient(
    ingredient=brokul, recipe=kurczakBrokul, massFraction=0.5)
new_recipeIngredient27.save()
new_recipeIngredient28 = RecipeIngredient(
    ingredient=orzechyW, recipe=jablkoOrzechy, massFraction=0.4)
new_recipeIngredient28.save()
new_recipeIngredient29 = RecipeIngredient(
    ingredient=jablko, recipe=jablkoOrzechy, massFraction=0.6)
new_recipeIngredient29.save()

new_recipeIngredient30 = RecipeIngredient(
    ingredient=awokado, recipe=salatkaSzpinak, massFraction=0.2)
new_recipeIngredient30.save()
new_recipeIngredient31 = RecipeIngredient(
    ingredient=slonecznik, recipe=salatkaSzpinak, massFraction=0.2)
new_recipeIngredient31.save()
new_recipeIngredient32 = RecipeIngredient(
    ingredient=oliwa, recipe=salatkaSzpinak, massFraction=0.2)
new_recipeIngredient32.save()
new_recipeIngredient33 = RecipeIngredient(
    ingredient=szpinak, recipe=salatkaSzpinak, massFraction=0.2)
new_recipeIngredient33.save()
new_recipeIngredient34 = RecipeIngredient(
    ingredient=pomidor, recipe=salatkaSzpinak, massFraction=0.2)
new_recipeIngredient34.save()

#
new_recipeIngredient = RecipeIngredient(
    ingredient=jajka, recipe=kanapkaAwokadoJajko, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=awokado, recipe=kanapkaAwokadoJajko, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=pieczywo, recipe=kanapkaAwokadoJajko, massFraction=0.3)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=platkiO, recipe=owsiankaOwoce, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=jogurt, recipe=owsiankaOwoce, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=borowki, recipe=owsiankaOwoce, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=truskawki, recipe=owsiankaOwoce, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=migdaly, recipe=owsiankaOwoce, massFraction=0.1)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=pieczywo, recipe=kanapkaSerekPomidory, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=serekW, recipe=kanapkaSerekPomidory, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=pomidor, recipe=kanapkaSerekPomidory, massFraction=0.4)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=jajka, recipe=omletJajeczny, massFraction=0.5)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=pomidor, recipe=omletJajeczny, massFraction=0.5)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=serekW, recipe=serekOwoce, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=maliny, recipe=serekOwoce, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=jagody, recipe=serekOwoce, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=banan, recipe=serekOwoce, massFraction=0.2)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=mleko, recipe=koktajlBananTruskawka, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=banan, recipe=koktajlBananTruskawka, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=truskawki, recipe=koktajlBananTruskawka, massFraction=0.3)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=jagody, recipe=koktajlJagoda, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=mlekoMigdalowe, recipe=koktajlJagoda, massFraction=0.6)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=truskawki, recipe=koktajlTruskawka, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=jogurt, recipe=koktajlTruskawka, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=mlekoMigdalowe, recipe=koktajlTruskawka, massFraction=0.4)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=banan, recipe=koktajlAwokado, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=awokado, recipe=koktajlAwokado, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=mleko, recipe=koktajlAwokado, massFraction=0.5)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=awokado, recipe=koktajlSzpinak, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=jablko, recipe=koktajlSzpinak, massFraction=0.5)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=szpinak, recipe=koktajlSzpinak, massFraction=0.2)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=losos, recipe=szaszlykLosos, massFraction=0.35)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=cukinia, recipe=szaszlykLosos, massFraction=0.25)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=papryka, recipe=szaszlykLosos, massFraction=0.25)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=cebula, recipe=szaszlykLosos, massFraction=0.15)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=kurczak, recipe=kurczakGrillWarzywa, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=cukinia, recipe=kurczakGrillWarzywa, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=papryka, recipe=kurczakGrillWarzywa, massFraction=0.3)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=jajka, recipe=salatkaJajkoKasza, massFraction=0.25)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=kaszaGryczana, recipe=salatkaJajkoKasza, massFraction=0.25)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=salata, recipe=salatkaJajkoKasza, massFraction=0.1)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=szczypior, recipe=salatkaJajkoKasza, massFraction=0.05)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=rzodkiewka, recipe=salatkaJajkoKasza, massFraction=0.15)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=suszonePomidory, recipe=salatkaJajkoKasza, massFraction=0.15)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=tilapia, recipe=tilapiaWarzywa, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=cukinia, recipe=tilapiaWarzywa, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=pomidor, recipe=tilapiaWarzywa, massFraction=0.3)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=tunczyk, recipe=tunczykSzparagi, massFraction=0.5)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=szparagi, recipe=tunczykSzparagi, massFraction=0.5)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=jablko, recipe=jablkoMasloOrzechowe, massFraction=0.7)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=masloOrzechowe, recipe=jablkoMasloOrzechowe, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=orzechyN, recipe=orzechyNerkowca, massFraction=1.0)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=jagody, recipe=jagodyMigdaly, massFraction=0.7)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=migdaly, recipe=jagodyMigdaly, massFraction=0.3)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=jablko, recipe=jablkoOrzechy, massFraction=0.7)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=orzechyW, recipe=jablkoOrzechy, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=banan, recipe=bananPodwieczorek, massFraction=1.0)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=jogurt, recipe=jogurtOtreby, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=banan, recipe=jogurtOtreby, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=otreby, recipe=jogurtOtreby, massFraction=0.2)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=pieczywo, recipe=kanapkaLosos, massFraction=0.6)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=maslo, recipe=kanapkaLosos, massFraction=0.05)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=lososWedzony, recipe=kanapkaLosos, massFraction=0.35)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=pomidor, recipe=salatkaCaprese, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=mozzarella, recipe=salatkaCaprese, massFraction=0.35)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=pieczywo, recipe=salatkaCaprese, massFraction=0.25)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=pieczywo, recipe=kanapkaAwokadoSzynka, massFraction=0.3)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=awokado, recipe=kanapkaAwokadoSzynka, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=szynka, recipe=kanapkaAwokadoSzynka, massFraction=0.15)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=pomidor, recipe=kanapkaAwokadoSzynka, massFraction=0.35)
new_recipeIngredient.save()
#
new_recipeIngredient = RecipeIngredient(
    ingredient=feta, recipe=kaszaJarmuz, massFraction=0.15)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=kaszaGryczana, recipe=kaszaJarmuz, massFraction=0.4)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=jarmuz, recipe=kaszaJarmuz, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=suszonePomidory, recipe=kaszaJarmuz, massFraction=0.2)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=czosnek, recipe=kaszaJarmuz, massFraction=0.025)
new_recipeIngredient.save()
new_recipeIngredient = RecipeIngredient(
    ingredient=oliwa, recipe=kaszaJarmuz, massFraction=0.025)
new_recipeIngredient.save()


new_menu = Menu(date_from=datetime.date(2020, 11, 16),
                date_to=datetime.date(2020, 11, 23), calories=1000)
new_menu.save()

new_client_menu = ClientMenu(client=new_client1, menu=new_menu)
new_client_menu.save()

new_meal1 = Meal(menu=new_menu, recipe=owsiankaPomarancza,
                 calories=300, date=datetime.date(2020, 11, 16))
new_meal1.save()
new_meal2 = Meal(menu=new_menu, recipe=kanapkaSzynkaPomidor,
                 calories=350, date=datetime.date(2020, 11, 16))
new_meal2.save()
new_meal3 = Meal(menu=new_menu, recipe=lososFasolkaPomidor,
                 calories=270, date=datetime.date(2020, 11, 16))
new_meal3.save()
new_meal4 = Meal(menu=new_menu, recipe=marchewkaPodwieczorek,
                 calories=400, date=datetime.date(2020, 11, 16))
new_meal4.save()
new_meal5 = Meal(menu=new_menu, recipe=serekPomidor,
                 calories=350, date=datetime.date(2020, 11, 16))
new_meal5.save()

new_meal6 = Meal(menu=new_menu, recipe=jajecznica,
                 calories=200, date=datetime.date(2020, 11, 17))
new_meal6.save()
new_meal7 = Meal(menu=new_menu, recipe=kanapkaSerOgorek,
                 calories=450, date=datetime.date(2020, 11, 17))
new_meal7.save()
new_meal8 = Meal(menu=new_menu, recipe=kurczakBrokul,
                 calories=170, date=datetime.date(2020, 11, 17))
new_meal8.save()
new_meal9 = Meal(menu=new_menu, recipe=jablkoOrzechy,
                 calories=300, date=datetime.date(2020, 11, 17))
new_meal9.save()
new_meal10 = Meal(menu=new_menu, recipe=salatkaSzpinak,
                  calories=250, date=datetime.date(2020, 11, 17))
new_meal10.save()

new_meal11 = Meal(menu=new_menu, recipe=kanapkaAwokadoJajko,
                  calories=300, date=datetime.date(2020, 11, 18))
new_meal11.save()
new_meal12 = Meal(menu=new_menu, recipe=koktajlBananTruskawka,
                  calories=350, date=datetime.date(2020, 11, 18))
new_meal12.save()
new_meal13 = Meal(menu=new_menu, recipe=szaszlykLosos,
                  calories=270, date=datetime.date(2020, 11, 18))
new_meal13.save()
new_meal14 = Meal(menu=new_menu, recipe=jablkoMasloOrzechowe,
                  calories=400, date=datetime.date(2020, 11, 18))
new_meal14.save()
new_meal15 = Meal(menu=new_menu, recipe=jogurtOtreby,
                  calories=350, date=datetime.date(2020, 11, 18))
new_meal15.save()

new_meal16 = Meal(menu=new_menu, recipe=owsiankaOwoce,
                  calories=200, date=datetime.date(2020, 11, 19))
new_meal16.save()
new_meal17 = Meal(menu=new_menu, recipe=koktajlJagoda,
                  calories=450, date=datetime.date(2020, 11, 19))
new_meal17.save()
new_meal18 = Meal(menu=new_menu, recipe=salatkaJajkoKasza,
                  calories=170, date=datetime.date(2020, 11, 19))
new_meal18.save()
new_meal19 = Meal(menu=new_menu, recipe=orzechyNerkowca,
                  calories=300, date=datetime.date(2020, 11, 19))
new_meal19.save()
new_meal20 = Meal(menu=new_menu, recipe=kanapkaLosos,
                  calories=250, date=datetime.date(2020, 11, 19))
new_meal20.save()

new_meal21 = Meal(menu=new_menu, recipe=kanapkaSerekPomidory,
                  calories=300, date=datetime.date(2020, 11, 20))
new_meal21.save()
new_meal22 = Meal(menu=new_menu, recipe=koktajlTruskawka,
                  calories=350, date=datetime.date(2020, 11, 20))
new_meal22.save()
new_meal23 = Meal(menu=new_menu, recipe=tunczykSzparagi,
                  calories=270, date=datetime.date(2020, 11, 20))
new_meal23.save()
new_meal24 = Meal(menu=new_menu, recipe=bananPodwieczorek,
                  calories=400, date=datetime.date(2020, 11, 20))
new_meal24.save()
new_meal25 = Meal(menu=new_menu, recipe=salatkaCaprese,
                  calories=350, date=datetime.date(2020, 11, 20))
new_meal25.save()

new_meal26 = Meal(menu=new_menu, recipe=omletJajeczny,
                  calories=200, date=datetime.date(2020, 11, 21))
new_meal26.save()
new_meal27 = Meal(menu=new_menu, recipe=koktajlAwokado,
                  calories=450, date=datetime.date(2020, 11, 21))
new_meal27.save()
new_meal28 = Meal(menu=new_menu, recipe=tilapiaWarzywa,
                  calories=170, date=datetime.date(2020, 11, 21))
new_meal28.save()
new_meal29 = Meal(menu=new_menu, recipe=jablkoMasloOrzechowe,
                  calories=300, date=datetime.date(2020, 11, 21))
new_meal29.save()
new_meal30 = Meal(menu=new_menu, recipe=kanapkaAwokadoSzynka,
                  calories=250, date=datetime.date(2020, 11, 21))
new_meal30.save()

new_meal31 = Meal(menu=new_menu, recipe=serekOwoce,
                  calories=300, date=datetime.date(2020, 11, 22))
new_meal31.save()
new_meal32 = Meal(menu=new_menu, recipe=koktajlSzpinak,
                  calories=350, date=datetime.date(2020, 11, 22))
new_meal32.save()
new_meal33 = Meal(menu=new_menu, recipe=kurczakGrillWarzywa,
                  calories=270, date=datetime.date(2020, 11, 22))
new_meal33.save()
new_meal34 = Meal(menu=new_menu, recipe=jagodyMigdaly,
                  calories=400, date=datetime.date(2020, 11, 22))
new_meal34.save()
new_meal35 = Meal(menu=new_menu, recipe=kaszaJarmuz,
                  calories=350, date=datetime.date(2020, 11, 22))
new_meal35.save()
