from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.RegistrationView.as_view()),
    path('client/get', views.ClientDataGetView.as_view()),
    path('client/save', views.ClientDataSaveView.as_view()),
    path('client/menu/', views.ClientMenuView.as_view()),
    path('client/diet/', views.DietGeneratorView.as_view()),
    path('client/<file>/', views.FileDownloader.as_view()),
    path('client/meal/info/', views.MealView.as_view()),
    path('recipes/', views.RecipesView.as_view()),
    path('recipe/image/', views.RecipeImageView.as_view()),
    path('recipe/new/', views.RecipeView.as_view()),
    path('ingredients/', views.IngredientsView.as_view()),
    path('allergens/', views.AllergensView.as_view()),
    path('documents/', views.DocumentsView.as_view())
]
