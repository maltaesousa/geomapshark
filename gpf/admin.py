from django.contrib.gis import admin
# Register your models here.
from .models import PermisFouille

admin.site.register(PermisFouille, admin.OSMGeoAdmin)
