import django_filters
from .models import AgencyProgramConfig, ProgramEligibility, Enrollment


class AgencyProgramConfigViewsetFilter(django_filters.FilterSet):
    class Meta:
        model = AgencyProgramConfig
        fields = ['agency', 'program']


class ProgramEligibilityViewsetFilter(django_filters.FilterSet):
    class Meta:
        model = ProgramEligibility
        fields = ['client']


class EnrollmentViewsetFilter(django_filters.FilterSet):
    class Meta:
        model = Enrollment
        fields = ['client', 'program']
