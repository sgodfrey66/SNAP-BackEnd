import django_filters
from .models import AgencyEligibilityConfig, ClientEligibility


class AgencyEligibilityConfigViewsetFilter(django_filters.FilterSet):
    class Meta:
        model = AgencyEligibilityConfig
        fields = ['agency']


class ClientEligibilityViewsetFilter(django_filters.FilterSet):
    class Meta:
        model = ClientEligibility
        fields = ['client']
