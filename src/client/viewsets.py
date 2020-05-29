from django.contrib.postgres.search import SearchVector, SearchQuery
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from core.viewsets import ModelViewSet
from core.permissions import IsAdmin, IsAgencyMember
from core.logging import RequestLogger
from .models import Client
from .serializers import ClientReader, ClientWriter


class ClientViewset(ModelViewSet):
    queryset = Client.objects.all()
    read_serializer_class = ClientReader
    write_serializer_class = ClientWriter
    permission_classes = [IsAdmin | IsAgencyMember]

    def get_queryset(self):
        return Client.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save(created_by=self.request.user)
        self.request.logger.set_context(
            data=serializer.validated_data,
            instance=instance,
        ).info('client created')

    def perform_update(self, serializer):
        instance = serializer.save()
        self.request.logger.set_context(
            data=serializer.validated_data,
            instance=instance,
        ).info('client updated')

    def perform_destroy(self, instance):
        instance.destroy()
        self.request.logger.set_context(
            instance=instance,
        ).info('client deleted')

    @action(detail=False, methods=['get'])
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=False,
                              description='Search string'),
        ],
    )
    def search(self, request):
        queryset = self.get_queryset()
        search_str = request.GET.get('q', None)
        search_query = SearchQuery(search_str + ':*', search_type='raw')
        if search_str:
            queryset = queryset.annotate(
                search=SearchVector('first_name', 'middle_name', 'last_name'),
            ).filter(search=search_query)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
