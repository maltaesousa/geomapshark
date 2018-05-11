# Create your models here.
from django.contrib.gis.db import models

class Intervenant(models.Model):
    objectid = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    npa = models.IntegerField()
    lieu = models.CharField(max_length=100)
    responsable = models.CharField(max_length=100)
    telephone = models.IntegerField()
    mobile = models.IntegerField()
    fax = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return str(self.objectid) + ' ' + self.nom

class Service(models.Model):
    objectid = models.AutoField(primary_key=True)
    archeologue = models.BooleanField()
    texteemail = models.TextField()
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    valideur = models.BooleanField()
    administrateur = models.BooleanField()

    def __str__(self):
        return str(self.objectid) + ' ' + self.nom

class TypeEmplacement(models.Model):
    objectid = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.objectid) + ' ' + self.description

class Demande(models.Model):
    objectid = models.AutoField(primary_key=True)
    paye = models.BooleanField()
    validetermine = models.BooleanField()
    datedebut = models.DateField()
    datefin = models.DateField()
    datefineffective = models.DateField()
    longueur = models.FloatField()
    largeur = models.FloatField()
    marquageroute = models.BooleanField()
    espacevert = models.BooleanField()
    factureentreprise = models.BooleanField()
    entreprise = models.ForeignKey(Intervenant, on_delete=models.SET_NULL, null=True, related_name='%(class)s_entreprise')
    maitreouvrage = models.ForeignKey(Intervenant, on_delete=models.SET_NULL, null=True, related_name='%(class)s_maitreouvrage')
    typeemplacement = models.ForeignKey(TypeEmplacement, on_delete=models.SET_NULL, null=True)
    description = models.TextField()

    def __str__(self):
        return str(self.objectid)

class Validation(models.Model):
    objectid = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    demande = models.ForeignKey(Demande, on_delete=models.CASCADE)
    effectue = models.BooleanField()
    accepte = models.BooleanField()
    remarque = models.TextField()

    def __str__(self):
            return str(self.objectid) + ' ' + str(self.service) + '-' + str(self.demande)

class PermisFouille(models.Model):
    objectid = models.AutoField(primary_key=True)
    hkoord  = models.FloatField()
    vkoord = models.FloatField()
    archeologique = models.IntegerField()
    archeologique_existant = models.IntegerField()
    rue_ref = models.IntegerField()
    ruenum_ref = models.IntegerField()
    demande = models.ForeignKey(Demande, on_delete=models.PROTECT)
    geom = models.PointField(srid=2056)

    # Returns the string representation of the model.
    def __str__(self):
        return str(self.objectid)
