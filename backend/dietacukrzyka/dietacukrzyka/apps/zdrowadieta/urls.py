from django.urls import path, include
from . import views

urlpatterns = [
    path('clients', views.ClientsView.as_view())
]