import django_filters
from django.core import exceptions
from rest_framework.exceptions import ValidationError


class AgencyFilter(django_filters.FilterSet):
    agency = django_filters.CharFilter(method='filter_by_agency')

    def filter_by_agency(self, qs, name, value):
        try:
            qs = qs.filter(agency_id=value)
        except exceptions.ValidationError as e:
            raise ValidationError({'agency': e.messages})
        return qs
