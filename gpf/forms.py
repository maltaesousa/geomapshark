from django.contrib.gis import forms
from .models import PermitRequest, Actor, Validation

class SitOpenLayersWidget(forms.OSMWidget):

    @property
    def media(self):
        return forms.Media(css={'all': ('libs/js/openlayers/ol.css',)},
                           js=('libs/js/openlayers/ol-debug.js', 'customWidgets/sitMapWidget/sitMapWidget.js'))

class PermitRequestForm(forms.ModelForm):
    class Meta:
        model = PermitRequest
        fields = '__all__'
        widgets = {
            'geom': SitOpenLayersWidget(attrs={
                'map_width': 800,
                'map_height': 500,
                'map_srid': 2056
                }
            )
        }

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'

class ValidationForm(forms.ModelForm):
    class Meta:
        model = Validation
        fields = '__all__'


ValidationFormSet = forms.inlineformset_factory(
    PermitRequest, Validation, form=ValidationForm, extra=1)
