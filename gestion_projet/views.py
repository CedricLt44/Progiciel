from django.shortcuts import render

# Create your views here.
def liste_projets(request):
    return render(request, 'gestion_projet/liste_projets.html')