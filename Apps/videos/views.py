from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .forms import VideosForm
from .models import Videos
from django.urls import reverse_lazy

class VideosView(ListView): # Renombramos la clase para mayor claridad y evitar conflictos
    model = Videos  # Especifica el modelo que quieres listar
    template_name = 'videos.html'  # El nombre de tu template
    context_object_name = 'lista_videos'  # El nombre de la variable que contendrá la lista en el template


class CrearVideoView(CreateView):
    template_name = 'crear.html'
    form_class = VideosForm
    success_url = reverse_lazy('videos:videosapp')