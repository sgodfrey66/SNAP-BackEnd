import django_filters
from django.core import exceptions
from rest_framework.exceptions import ValidationError
from .models import AgencyProgramConfig, Eligibility, Enrollment


class AgencyProgramConfigViewsetFilter(django_filters.FilterSet):
    class Meta:
        model = AgencyProgramConfig
        fields = ['agency', 'program']


class EligibilityViewsetFilter(django_filters.FilterSet):
    class Meta:
        model = Eligibility
        fields = ['client']


class EnrollmentViewsetFilter(django_filters.FilterSet):
    class Meta:
        model = Enrollment
        fields = ['client']
