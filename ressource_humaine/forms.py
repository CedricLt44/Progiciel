from django import forms
from .models import Employe
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
            'date_obtention_diplome': forms.DateInput(attrs={'type': 'date'}),  # Champ Date pour 'date_obtention_diplome'
            'date_obtention_caces': forms.DateInput(attrs={'type': 'date'}),  # Champ Date pour 'date_obtention_caces'
            'date_expiration_caces': forms.DateInput(attrs={'type': 'date'}),  # Champ Date pour 'date_expiration_caces'
            'date_obtention_permis': forms.DateInput(attrs={'type': 'date'}),  # Champ Date pour 'date_obtention_permis'
            'date_debut': forms.DateInput(attrs={'type': 'date'}),  # Champ Date pour 'date_debut_contrat'
            'date_fin': forms.DateInput(attrs={'type': 'date'}),  # Champ Date pour 'date_fin_contrat'
        }

    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),  # Liste des groupes disponibles
        required=False,  # Champ non obligatoire
        widget=forms.Select(attrs={'class': 'form-control'}),  # Ajout de classes CSS pour le style
    )
