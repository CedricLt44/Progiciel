from django.shortcuts import render

# Create your views here.
def liste_employe(request):
    return render(request, 'ressource_humaine/liste_employe.html')