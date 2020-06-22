from core.viewsets import ModelViewSet
from core.permissions import IsAdmin, IsAgencyMember
from .models import Note
from .serializers import NoteReader, NoteWriter
from .filters import NoteFilter


class NoteViewset(ModelViewSet):
    queryset = Note.objects.all()
    read_serializer_class = NoteReader
    write_serializer_class = NoteWriter
    permission_classes = [IsAdmin | IsAgencyMember]
    filterset_class = NoteFilter

    # def get_queryset(self):
    #     return Note.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
