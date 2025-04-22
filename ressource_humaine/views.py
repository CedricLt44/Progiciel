from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Employe
from .forms import EmployeForm

@login_required
def liste_employe(request):
    """
    Affiche la liste des employés filtrée par groupe.
    """
    # Récupérer tous les groupes de l'utilisateur
    user_groups = request.user.groups.all()

    # Filtrer les employés par groupe si l'utilisateur appartient à un ou plusieurs groupes
    if user_groups:
        # Si un groupe est sélectionné, filtrer les employés par ce groupe
        employes = Employe.objects.filter(group__in=user_groups)
    else:
        # Si aucun groupe n'est sélectionné, afficher tous les employés
        employes = Employe.objects.all()

    # Passer les employés et groupes dans le contexte
    return render(request, 'ressource_humaine/liste_employe.html', {'employes': employes, 'user_groups': user_groups})

@login_required
def add_employe(request):
    """
    Vue permettant d'ajouter un employé.
    """
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            # Sauvegarde de l'employé
            employe = form.save()

            # Assurez-vous d'ajouter l'employé aux groupes choisis (si applicable)
            groups = form.cleaned_data.get('group')  # Récupère les groupes sélectionnés
            employe.groups.set(groups)  # Associe les groupes à l'employé
            employe.save()

            return redirect('ressource_humaine:liste_employe')  # Redirige vers la liste des employés après l'ajout
    else:
        form = EmployeForm()

    return render(request, 'ressource_humaine/add_employe.html', {'form': form})