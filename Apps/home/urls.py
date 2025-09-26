
from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from Apps.home import views

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='homeapp'),
]
