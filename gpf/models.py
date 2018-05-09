
# Create your models here.
from django.contrib.gis.db import models
from django.forms import ModelForm
from django.contrib.gis import forms

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

class PermisFouille(models.Model):

    objectid = models.IntegerField()
    hkoord  = models.FloatField()
    vkoord = models.FloatField()
    archeologique = models.IntegerField()
    archeologique_existant = models.IntegerField()
    rue_ref = models.IntegerField()
    ruenum_ref = models.IntegerField()
    demande_ref = models.IntegerField()
    geom = models.PointField(srid=2056)


    # Returns the string representation of the model.
    def __str__(self):
        return str(self.objectid)

class SitOpenLayersWidget(forms.OpenLayersWidget):
    class Media:
        js = ('openlayers.js')

class PermisFouilleForm(forms.Form):
    geom = forms.PointField(widget=
        forms.OpenLayersWidget(attrs={
            'map_width': 800,
            'map_height': 500,
            'map_srid': 2056}))
    # class Meta:
    #     model = PermisFouille
    #     fields = ['objectid', 'geom']
