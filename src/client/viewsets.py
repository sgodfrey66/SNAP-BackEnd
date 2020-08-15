from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from core.viewsets import ModelViewSet
from core.permissions import IsAdmin, IsAgencyMember
from core.logging import RequestLogger
from .models import Client
from .serializers import ClientReader, ClientWriter
from .filters import ClientSearchFilter, AgencyClientSearchFilter


class ClientViewset(ModelViewSet):
    queryset = Client.objects.all()
    read_serializer_class = ClientReader
    write_serializer_class = ClientWriter
    permission_classes = [IsAdmin | IsAgencyMember]
    filterset_class = AgencyClientSearchFilter

    ordering_fields = ['first_name', 'middle_name', 'last_name', 'dob']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
