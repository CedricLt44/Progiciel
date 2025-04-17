from django.urls import path

from . import views

app_name = 'ressource_humaine'

urlpatterns = [
    path('ressource_humaine/', views.liste_employe, name='liste_employe'),
]