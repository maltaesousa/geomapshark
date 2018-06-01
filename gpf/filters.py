import django_filters
from .models import PermitRequest

class PermitRequestFilter(django_filters.FilterSet):
    class Meta:
        model = PermitRequest
        fields = ['date_end', 'date_start','project_owner', 'road_ref', 'validated', 'paid']
