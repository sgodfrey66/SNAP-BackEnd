from core.viewsets import ModelViewSet
from .models import Client
from .serializers import ClientReader, ClientWriter
from core.permissions import IsAgencyMember


class ClientViewset(ModelViewSet):
    queryset = Client.objects.all()
    read_serializer_class = ClientReader
    write_serializer_class = ClientWriter
    permission_classes = [IsAgencyMember]

    def get_queryset(self):
        return Client.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
