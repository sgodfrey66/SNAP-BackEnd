from core.viewsets import ModelViewSet
from core.permissions import IsAgencyMember
from .models import Survey
from .serializers import SurveyReader, SurveyWriter


class SurveyViewset(ModelViewSet):
    queryset = Survey.objects.all()
    read_serializer_class = SurveyReader
    write_serializer_class = SurveyWriter
    permission_classes = [IsAgencyMember]

    def get_queryset(self):
        return Survey.objects.for_user(self.request.user)
