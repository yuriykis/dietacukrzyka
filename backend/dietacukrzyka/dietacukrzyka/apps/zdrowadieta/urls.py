from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.RegistrationView.as_view()),
    path('client/get', views.ClientDataGetView.as_view()),
    path('client/save', views.ClientDataSaveView.as_view()),
    path('client/<meal_type>/ingredients_weight/<menu_date>', views.ClientGenerateIngredientsWeight.as_view()),
    path('menu/<meal_type>/<menu_date>/', views.ClientMenuView.as_view()),
    path('menu/ingredients/<meal_type>/<menu_date>/', views.ClientMenuIngredientsView.as_view())
]