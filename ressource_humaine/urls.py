from django.urls import path

from . import views

app_name = 'ressource_humaine'

urlpatterns = [
    path('ressource_humaine/', views.liste_employe, name='liste_employe'),
    path('add/', views.add_employe, name='add_employe'),
    path('employe/<int:employe_id>/', views.detail_employe, name='detail_employe'),

]