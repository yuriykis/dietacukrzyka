from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.RegistrationView.as_view()),
    path('client/get', views.ClientDataGetView.as_view()),
    path('client/save', views.ClientDataSaveView.as_view()),
    path('menu/<meal_type>/', views.ClientMenuView.as_view())
]