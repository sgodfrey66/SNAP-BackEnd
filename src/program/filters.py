import django_filters
from .models import Program, ProgramEligibility, Enrollment


class ProgramViewsetFilter(django_filters.FilterSet):
    class Meta:
        model = Program
        fields = ['agency']


class ProgramEligibilityViewsetFilter(django_filters.FilterSet):
    class Meta:
        model = ProgramEligibility
        fields = ['client']


class EnrollmentViewsetFilter(django_filters.FilterSet):
    class Meta:
        model = Enrollment
        fields = ['client', 'program']
