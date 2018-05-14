from django.forms import modelformset_factory, ModelForm
from django.contrib.gis import forms

class SitOpenLayersWidget(forms.OpenLayersWidget):
    class Media:
        js = ('openlayers.js')

class PermisFouilleForm(forms.Form):
    geom = forms.PointField(widget=
        forms.OpenLayersWidget(attrs={
            'map_width': 800,
            'map_height': 500,
            'map_srid': 2056}))
