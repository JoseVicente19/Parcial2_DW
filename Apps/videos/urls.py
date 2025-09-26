
from django.contrib import admin
from django.urls import path, include
from .views import VideosView, CrearVideoView
from Apps.videos import views

app_name = 'videos'

urlpatterns = [
    path('', VideosView.as_view(), name='videosapp'),
    path('crear/', CrearVideoView.as_view(), name='crear')

]
