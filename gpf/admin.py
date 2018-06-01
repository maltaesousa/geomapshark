from django.contrib.gis import admin
from .models import *

admin.site.register(PermitRequest, admin.OSMGeoAdmin)
admin.site.register(Actor)
admin.site.register(Department)
admin.site.register(SiteType)
admin.site.register(Validation)
admin.site.register(Archelogy)
admin.site.register(CreditorType)
