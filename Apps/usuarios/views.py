from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .forms import UsuarioForm
from .models import Usuario
from django.urls import reverse_lazy

class UsuariosView(ListView): # Renombramos la clase para mayor claridad y evitar conflictos
    model = Usuario  # Especifica el modelo que quieres listar
    template_name = 'usuarios.html'  # El nombre de tu template
    context_object_name = 'lista_usuarios'  # El nombre de la variable que contendrá la lista en el template


class CrearUsuarioView(CreateView):
    template_name = 'crearu.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('usuarios:usuariosapp')