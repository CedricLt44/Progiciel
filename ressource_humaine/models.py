from django.db import models
from django.contrib.auth.models import Group

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

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Diplome(models.Model):
    """
    Diplômes obtenus par un employé.
    """
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='diplomes')
    nom_diplome = models.CharField(max_length=100)
    date_obtention = models.DateField()

    def __str__(self):
        return f"{self.nom} ({self.employe})"
    
class CACES(models.Model):
    """
    CACES détenus par un employé.
    """
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='caces')
    type_caces = models.CharField(max_length=50)
    date_obtention = models.DateField()
    date_expiration = models.DateField()

    def __str__(self):
        return f"CACES {self.type} - {self.employe}"


class Permis(models.Model):
    """
    Permis de conduire détenus par un employé.
    """
    TYPE_PERMIS = [
    ('A', 'A (Moto)'),
    ('B', 'B (Voiture)'),
    ('C', 'C (Poids lourd)'),
    ('D', 'D (Transport en commun)'),
    ('BE', 'BE (Voiture + Remorque)'),
    ]

    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='permis')
    type_permis = models.CharField(max_length=20, choices=TYPE_PERMIS)  # Ex: B, C, D
    date_obtention = models.DateField()

    def __str__(self):
        return f"Permis {self.type} - {self.employe}"

# Modèle Contrat
class Contrat(models.Model):
    TYPE_CHOICES = [
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('Stage', 'Stage'),
        ('Alternance', 'Alternance')
    ]
    
    employe = models.OneToOneField(Employe, on_delete=models.CASCADE)
    type_contrat = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.type_contrat} - {self.employe}"