from core.viewsets import ModelViewSet
from core.permissions import IsAdmin, IsAgencyMemberReadOnly
from .models import Program
from .serializers import ProgramReader, ProgramWriter
# from .filters import AgencyFilter


class ProgramViewset(ModelViewSet):
    queryset = Program.objects.all()
    read_serializer_class = ProgramReader
    write_serializer_class = ProgramWriter
    permission_classes = [IsAdmin | IsAgencyMemberReadOnly]

    def get_queryset(self):
        return Program.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
