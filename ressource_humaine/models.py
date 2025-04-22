from django.db import models
from django.contrib.auth.models import Group
from django.conf import settings
# Create your models here.
# modèle DEpartement
class Departement(models.Model):
    """
    Modèle représentant les différents départements de l'entreprise.
    Ce modèle est prérempli via une migration personnalisée.
    """
    TYPE_CHOICES = [
    ('DIRECTION', 'DIR'),
    ('RESSORCE HUMAINE', 'RH'),
    ('INFORMATIQUE', 'IT'),
    ('MARKETING', 'MARKET'),
    ('COMPTABILITE', 'COMPTA'),
    ('PRODUCTION', 'PROD'),
    ]
    nom_departement= models.CharField(choices=TYPE_CHOICES, default='RH')

    def __str__(self):
        return self.nom_departement

class Employe(models.Model):
    """
    Modèle représentant un employé.
    """
    CIVILITE_CHOICES = [('M', 'Monsieur'), ('F', 'Madame')]

    civilite = models.CharField(max_length=1, choices=CIVILITE_CHOICES, default='M')
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=250,blank=True)
    ville = models.CharField(max_length=100, blank=True)
    code_postal = models.CharField(max_length=10, blank=True)
    pays = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    numero_securite_sociale = models.CharField(max_length=15, blank=True)
    date_embauche = models.DateField()
    poste = models.CharField(max_length=100)
    departement = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True, related_name="employes")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    # Diplômes obtenus par un employé.
    nom_diplome = models.CharField(max_length=100)
    date_obtention_diplome = models.DateField()
    # CACES détenus par un employé.
    TYPE_CACES = [
        ('R489-1A', 'Transpalettes à conducteur porté'),
        ('R489-1b', 'Gerbeurs à conducteur porté'),
        ('R489-cat-3', 'Chariots élévateur (6T)'),
        ('R489-cat-5', 'Chariots élévateurs à mât rétractable'),
        ('R482', 'Engin de chantier'),
        ('R490', 'Grues auxiliaires'),
        ('R486', 'Nacelle'),
    ]
    type_caces = models.CharField(max_length=20, choices=TYPE_CACES)  # Ex: R389, R482, R490    
    date_obtention_caces = models.DateField()
    date_expiration_caces = models.DateField()
    # Permis de conduire détenus par un employé.
    TYPE_PERMIS = [
    ('A', 'A (Moto)'),
    ('B', 'B (Voiture)'),
    ('C', 'C (Poids lourd)'),
    ('D', 'D (Transport en commun)'),
    ('BE', 'BE (Voiture + Remorque)'),
    ]
    type_permis = models.CharField(max_length=20, choices=TYPE_PERMIS)  # Ex: B, C, D
    date_obtention_permis = models.DateField()

    # Contrat de travail d'un employé.
    TYPE_CHOICES = [
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('Stage', 'Stage'),
        ('Alternance', 'Alternance')
    ]
    
    type_contrat = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date_debut = models.DateField()
    date_fin = models.DateField()
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"{self.prenom} {self.nom}"
