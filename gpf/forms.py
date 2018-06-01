from django.conf import settings
from django.contrib.gis import forms
from django.forms import widgets
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import PermitRequest, Actor, Validation


class SitOpenLayersWidget(forms.OSMWidget):
    @property
    def media(self):
        return forms.Media(
            css={'all': ('libs/js/openlayers/ol.css',)},
            js=('libs/js/openlayers/ol-debug.js',
                'customWidgets/sitMapWidget/sitMapWidget.js'))


class RelatedFieldWidgetCanAdd(widgets.Select):
    def __init__(self, related_model, related_url=None, *args, **kw):
        super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)

        if not related_url:
            rel_to = related_model
            info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
            related_url = 'admin:%s_%s_add' % info

        # Be careful that here "reverse" is not allowed
        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse(self.related_url)
        output = [super(RelatedFieldWidgetCanAdd, self).render(name, value, *args, **kwargs)]
        output.append(
            '<a href="%s" class="add-another" id="add_id_%s" \
            onclick="return showAddAnotherPopup(this);">Add Another</a>' % \
            (self.related_url, name))
        output.append(
            '<a id="edit_actor" style="cursor: pointer; cursor: hand;">Edit</a>'
        )
        return mark_safe(''.join(output))


class AddPermitRequestForm(forms.ModelForm):
    class Meta:
        model = PermitRequest
        fields = [
            'geom', 'description', 'date_start', 'date_end', 'sitetype',
            'length', 'width', 'road_marking_damaged', 'is_green_area',
            'project_owner', 'invoice_to'
        ]
        widgets = {
            'geom': SitOpenLayersWidget(attrs={
                'map_width': 800,
                'map_height': 500,
                'map_srid': 2056
            }),
            'date_start': forms.SelectDateWidget(),
            'date_end': forms.SelectDateWidget(),
            'date_effective_end': forms.SelectDateWidget(),
            'project_owner': RelatedFieldWidgetCanAdd(Actor, related_url='gpf:actor_add')
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
