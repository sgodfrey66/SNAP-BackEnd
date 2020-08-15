from core.viewsets import ModelViewSet
from .models import SecurityGroupUserAgency
from .serializers import SecurityGroupUserAgencyReader


class SecurityGroupUserAgencyViewset(ModelViewSet):
    queryset = SecurityGroupUserAgency.objects.all()
    read_serializer_class = SecurityGroupUserAgencyReader
    write_serializer_class = SecurityGroupUserAgencyReader

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
