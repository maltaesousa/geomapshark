from django.contrib.gis import admin
from .models import * 

admin.site.register(PermisFouille, admin.OSMGeoAdmin)
admin.site.register(Demande)
admin.site.register(Intervenant)
admin.site.register(Service)
admin.site.register(TypeEmplacement)
admin.site.register(Validation)
