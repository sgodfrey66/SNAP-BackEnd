from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from core.viewsets import ModelViewSet
from core.permissions import IsAdmin, IsAgencyMember
from core.logging import RequestLogger
from .models import Client
from .serializers import ClientReader, ClientWriter
from .filters import ClientFilter


class ClientViewset(ModelViewSet):
    queryset = Client.objects.all()
    read_serializer_class = ClientReader
    write_serializer_class = ClientWriter
    permission_classes = [IsAdmin | IsAgencyMember]
    filter_class = ClientFilter

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
