import django_filters
from django.core import exceptions
from rest_framework.exceptions import ValidationError
from django.contrib.postgres.search import SearchVector, SearchQuery
from .models import Client
from agency.models import AgencyClient
from security.models import SecurityGroupUserAgency
from django.db.models import Q


class ClientSearchFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_client')

    def search_client(self, qs, name, value):
        search_query = SearchQuery(value + ':*', search_type='raw')
        if value:
            qs = qs.annotate(
                search=SearchVector('first_name', 'middle_name', 'last_name'),
            ).filter(search=search_query)
        return qs


class ClientFilter(django_filters.FilterSet):
    client = django_filters.CharFilter(method='filter_by_client')

    def filter_by_client(self, qs, name, value):
        try:
            qs = qs.filter(client_id=value)
        except exceptions.ValidationError as e:
            raise ValidationError({'client': e.messages})
        return qs


class AgencyClientSearchFilter(django_filters.FilterSet):
    class Meta:
            model = Client
            fields = ['last_name', 'first_name', 'dob']

    @property
    def qs(self):
        parent = super().qs

        # Get the agency-groups for this user
        user = self.request.user
        sgua = SecurityGroupUserAgency.objects.filter(user_ref_id=user.id)

        # Get a list of the agencies for which this user has a role; since
        #  all roles have view permission we only need to the agencies (but we
        #  could look at specific permissions if needed
        agencies = [s.agency_ref.ref_id for s in sgua]

        q_objects = Q()
        # Create an 'or' query for all agencies for which this user has a role
        for a in agencies:
            q_objects |= Q(agency_ref=a)

        # Search the agency-client mapping for clients that also have these agencies
        result = AgencyClient.objects.filter(q_objects)

        q_objects = Q()
        # Create an 'or' query for the client ids in the previous query
        for c in [ac.client_id for ac in result]:
            q_objects |= Q(id=c)

        # result = AgencyClient.objects.filter(**filters)
        qs = parent.filter(q_objects)

        return qs
