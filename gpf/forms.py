from django.conf import settings
from django.contrib.gis import forms
from django.forms import widgets
from django.urls import reverse
from django.utils.safestring import mark_safe
from bootstrap_datepicker.widgets import DatePicker

from .models import PermitRequest, Actor, Validation

class SitOpenLayersWidget(forms.OSMWidget):
    template_name = 'openlayers/openlayers.html'
    @property
    def media(self):
        return forms.Media(
            css={'all': ('libs/js/openlayers/ol.css',)},
            js=('libs/js/openlayers/ol-debug.js',
                'libs/js/proj4js/proj4-src.js',
                'customWidgets/sitMapWidget/sitMapWidget.js'))


class AddPermitRequestForm(forms.ModelForm):
    class Meta:
        model = PermitRequest
        fields = [
            'geom', 'description', 'date_start', 'date_end', 'sitetype',
            'length', 'width', 'road_marking_damaged', 'is_green_area',
            'invoice_to'
        ]
        widgets = {
            'geom': SitOpenLayersWidget(attrs={
                'map_width': 800,
                'map_height': 500,
                'map_srid': 2056,
                'default_lon': 6.64513,
                'default_lat': 46.77808,
                'default_zoom': 15
            }),
            'date_start': DatePicker(
                options={
                    "format": "mm/dd/yyyy",
                    "autoclose": True
                    }
                ),
            'date_end': DatePicker(
                options={
                    "format": "mm/dd/yyyy",
                    "autoclose": True
                    }
                ),
            'date_effective_end': forms.SelectDateWidget(),
        }


class ChangePermitRequestForm(forms.ModelForm):
    class Meta:
        model = PermitRequest
        exclude = []
        widgets = {
            'geom': SitOpenLayersWidget(attrs={
                'map_width': 800,
                'map_height': 500,
                'map_srid': 2056
            }),
            'date_start': forms.SelectDateWidget(),
            'date_end': forms.SelectDateWidget(),
            'date_effective_end': forms.SelectDateWidget()
        }


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        exclude = ['user']


class ValidationForm(forms.ModelForm):
    class Meta:
        model = Validation
        fields = '__all__'


ValidationFormSet = forms.inlineformset_factory(
    PermitRequest, Validation, form=ValidationForm, extra=1)
