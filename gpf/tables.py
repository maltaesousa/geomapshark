import django_tables2 as tables

from .models import PermitRequest

class PermitRequestTable(tables.Table):

    edit_entries = tables.TemplateColumn('<a href="{% url \'gpf:permitdetail\' record.id %}">Edit</a>')

    class Meta:
        model = PermitRequest
        fields = ('date_start', 'date_end', 'date_effective_end', 'paid', 'validated',
            'road_marking_damaged', 'is_green_area', 'has_archeology', 'has_existing_archeology', 'road_ref', 'road_number_ref')
        template_name = 'django_tables2/bootstrap.html'

class PermitExportTable(tables.Table):

    class Meta:
        model = PermitRequest
        template_name = 'django_tables2/bootstrap.html'
