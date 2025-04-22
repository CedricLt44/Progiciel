from django import forms
from .models import Employe, Departement, Diplome, CACES, Permis, Contrat
from django.contrib.auth.models import Group

# Formulaire pour le modèle Employe
class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = '__all__'  # Inclut tous les champs du modèle
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),  # Champ Date pour 'date_naissance'
            'date_embauche': forms.DateInput(attrs={'type': 'date'}),   # Champ Date pour 'date_embauche'
            'telephone': forms.TextInput(attrs={'type': 'tel'}),  # Si tu veux spécifier un champ de type téléphone
            'email': forms.EmailInput(attrs={'type': 'email'}),   # Champ Email avec validation
            'numero_securite_sociale': forms.TextInput(attrs={'type': 'text', 'maxlength': '15'}),  # Limite de caractères pour le N° de sécurité sociale
        }
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),  # Liste des groupes disponibles
        required=False,  # Champ non obligatoire
        widget=forms.Select(attrs={'class': 'form-control'}),  # Ajout de classes CSS pour le style
    )
# Formulaire pour le modèle Departement
class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['nom_departement'] # Inclut les champs nécessaires



# Formulaire pour le modèle Diplome
class DiplomeForm(forms.ModelForm):
    class Meta:
        model = Diplome
        fields = '__all__'
        widgets = {
            'date_obtention': forms.DateInput(attrs={'type': 'date'}),
        }

# Formulaire pour le modèle CACES
class CACESForm(forms.ModelForm):
    class Meta:
        model = CACES
        fields = '__all__'
        widgets = {
            'date_obtention': forms.DateInput(attrs={'type': 'date'}),
            'date_expiration': forms.DateInput(attrs={'type': 'date'}),
        }

# Formulaire pour le modèle Permis
class PermisForm(forms.ModelForm):
    class Meta:
        model = Permis
        fields = '__all__'
        widgets = {
            'date_obtention': forms.DateInput(attrs={'type': 'date'}),
        }

# Formulaire pour le modèle Contrat
class ContratForm(forms.ModelForm):
    class Meta:
        model = Contrat
        fields = '__all__'
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }
