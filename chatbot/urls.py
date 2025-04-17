from django.urls import path
from . import views

app_name = 'chatbot'  # Nom de l'application pour le namespace

urlpatterns = [
    path('', views.chatbot_page, name='chatbot_page'),  # Affiche la page HTML
]
