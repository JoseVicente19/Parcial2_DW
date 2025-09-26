
from django.contrib import admin
from django.urls import path, include
from .views import UsuariosView, CrearUsuarioView
from Apps.usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('', UsuariosView.as_view(), name='usuariosapp'),
    path('crearu/', CrearUsuarioView.as_view(), name='crearu')

]
