import django_filters
from django.core import exceptions
from rest_framework.exceptions import ValidationError
from .models import Eligibility, Enrollment


class AgencyFilter(django_filters.FilterSet):
    agency = django_filters.CharFilter(method='filter_by_agency')

    def filter_by_agency(self, qs, name, value):
        try:
            qs = qs.filter(agency_id=value)
        except exceptions.ValidationError as e:
            raise ValidationError({'agency': e.messages})
        return qs


class ProgramFilter(django_filters.FilterSet):
    program = django_filters.CharFilter(method='filter_by_program')

    def filter_by_program(self, qs, name, value):
        try:
            qs = qs.filter(program_id=value)
        except exceptions.ValidationError as e:
            raise ValidationError({'program': e.messages})
        return qs


class EligibilityViewsetFilter(django_filters.FilterSet):
    class Meta:
        model = Eligibility
        fields = ['client']


class EnrollmentViewsetFilter(django_filters.FilterSet):
    class Meta:
        model = Enrollment
        fields = ['client']
