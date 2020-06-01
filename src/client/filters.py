import django_filters
from django.contrib.postgres.search import SearchVector, SearchQuery


class ClientFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_client')

    def search_client(self, qs, name, value):
        search_query = SearchQuery(value + ':*', search_type='raw')
        if value:
            qs = qs.annotate(
                search=SearchVector('first_name', 'middle_name', 'last_name'),
            ).filter(search=search_query)
        return qs
