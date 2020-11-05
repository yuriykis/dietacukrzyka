from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.RegistrationView.as_view()),
    path('client/get', views.ClientDataGetView.as_view()),
    path('client/save', views.ClientDataSaveView.as_view()),
    path('client/menu/', views.ClientMenuView.as_view()),
    path('client/<file>/', views.FileDownloader.as_view()),
    path('recipes/', views.RecipesView.as_view()),
    path('ingredients/', views.IngredientsView.as_view())
]
