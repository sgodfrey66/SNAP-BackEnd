from django.core import exceptions
import django_filters
from rest_framework.exceptions import ValidationError
from client.models import Client


class ResponseFilter(django_filters.FilterSet):
    client = django_filters.CharFilter(method='filter_by_client')

    def filter_by_client(self, qs, name, value):
        try:
            qs = qs.filter(respondent_id=value)
        except exceptions.ValidationError as e:
            raise ValidationError({'client': e.messages})
        return qs
