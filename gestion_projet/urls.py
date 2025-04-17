from django.urls import path

from . import views

app_name = 'gestion_projet'

urlpatterns = [
  path('liste_projets/' ,views.liste_projets, name='liste_projets'),
  ]