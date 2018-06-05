from django.db import models
import django_filters
from django_filters.widgets import RangeWidget
from .models import PermitRequest
from bootstrap_datepicker.widgets import DatePicker

class PermitRequestFilter(django_filters.FilterSet):

    date_end = django_filters.DateFromToRangeFilter(
        widget=DatePicker(
            options={
                "format": "mm/dd/yyyy",
                "autoclose": True
                }
            )
    )

    date_start = django_filters.RangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}))

    class Meta:
        model = PermitRequest
        fields = ['date_end', 'date_start','project_owner', 'road_ref', 'validated', 'paid']
