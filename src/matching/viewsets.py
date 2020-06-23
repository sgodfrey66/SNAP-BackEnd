from core.viewsets import ModelViewSet
from core.permissions import IsAdmin, IsAgencyMember
from .models import MatchingConfig, ClientMatching
from .serializers import (
    MatchingConfigReader, MatchingConfigWriter,
    ClientMatchingReader, ClientMatchingWriter,
)


class MatchingConfigViewset(ModelViewSet):
    queryset = MatchingConfig.objects.all()
    read_serializer_class = MatchingConfigReader
    write_serializer_class = MatchingConfigWriter
    permission_classes = [IsAdmin | IsAgencyMember]
    # filterset_class = ...

    # def get_queryset(self):
    #     return MatchingConfig.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ClientMatchingViewset(ModelViewSet):
    queryset = ClientMatching.objects.all()
    read_serializer_class = ClientMatchingReader
    write_serializer_class = ClientMatchingWriter
    permission_classes = [IsAdmin | IsAgencyMember]
    # filterset_class = ...

    # def get_queryset(self):
    #     return MatchingConfig.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
