# Create your models here.
from django.contrib.gis.db import models
from django.contrib.auth.models import User, Group

class Actor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    zipcode = models.IntegerField(null=True)
    city = models.CharField(max_length=100, null=True)
    person_in_charge = models.CharField(max_length=100, null=True)
    phone_fixed = models.IntegerField(null=True)
    phone_mobile = models.IntegerField(null=True)
    fax = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Department(models.Model):
    #Extend group model
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    email_content = models.TextField()
    #TODO: Put this things into groups
    is_validator = models.BooleanField()
    is_admin = models.BooleanField()
    is_archeologist = models.BooleanField()

    def __str__(self):
        return str(self.user)

class SiteType(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class PermitRequest(models.Model):
    paid = models.BooleanField()
    validated = models.BooleanField()
    date_start = models.DateField()
    date_end = models.DateField()
    date_effective_end = models.DateField(null=True)
    length = models.FloatField()
    width = models.FloatField()
    has_road_marking = models.BooleanField()
    is_green_area = models.BooleanField()
    invoiced = models.BooleanField()
    company = models.ForeignKey(Actor, on_delete=models.SET_NULL, null=True, related_name='%(class)s_company')
    project_owner = models.ForeignKey(Actor, on_delete=models.SET_NULL, null=True, related_name='%(class)s_project_owner')
    sitetype = models.ForeignKey(SiteType, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    has_archeology = models.BooleanField()
    has_existing_archeology = models.BooleanField()
    road_ref = models.IntegerField(null=True)
    road_number_ref = models.IntegerField(null=True)
    geom = models.MultiPointField(srid=2056)

    def __str__(self):
        return 'Permit ' + str(self.id)

class Validation(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    permitrequest = models.ForeignKey(PermitRequest, on_delete=models.CASCADE)
    done = models.BooleanField()
    accepted = models.BooleanField()
    comment = models.TextField(null=True)

    def __str__(self):
        return str(self.department) + '-' + str(self.permitrequest)

class Archelogy(models.Model):

    fiche = models.TextField(null=True)
    commune = models.TextField(null=True)
    descriptio = models.TextField(null=True)
    note_carto = models.TextField(null=True)
    annee_revi = models.TextField(null=True)
    id_per = models.TextField(null=True)
    lien_img = models.TextField(null=True)
    note_detai = models.TextField(null=True)
    shape_len = models.TextField(null=True)
    date_maj = models.TextField(null=True)
    guid = models.TextField(null=True)
    mention = models.TextField(null=True)
    fme_feat = models.TextField(null=True)
    autre_ment = models.TextField(null=True)
    multi_read = models.TextField(null=True)
    autre_mesu = models.TextField(null=True)
    shape_area = models.TextField(null=True)
    objectid = models.TextField(null=True)
    date_mesur = models.TextField(null=True)
    eca = models.TextField(null=True)
    url_recens = models.TextField(null=True)
    mesure = models.TextField(null=True)
    import_date = models.IntegerField(null=True)
    geom = models.MultiPolygonField(srid=2056)

    def __str__(self):
        return 'Archelogy' + str(self.id)
