from django.contrib import admin

# Register your models here.
from .models import Employe,Departement

class DepartementAdmin(admin.ModelAdmin):
    list_display = ('nom_departement',)  # Affiche le nom et le type de département dans la liste
    list_filter = ('nom_departement',)  # Permet de filtrer par type de département

class EmployeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'get_group','get_created_by')  # Affiche le groupe dans la liste des employés
    list_filter = ('group',)  # Permet de filtrer les employés par groupe

        # Méthode pour afficher le nom du groupe d'un employé
    def get_group(self, obj):
        return obj.group.name if obj.group else "Aucun groupe"
    get_group.short_description = 'Groupe'

    # Méthode pour afficher le nom d'utilisateur du créateur de l'employé
    def get_created_by(self, obj):
        return obj.created_by.email if obj.created_by else "Aucun créateur"
    get_created_by.short_description = 'Créé par'


admin.site.register(Employe, EmployeAdmin)
admin.site.register(Departement, DepartementAdmin)