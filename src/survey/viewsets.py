from core.viewsets import ModelViewSet
from core.permissions import IsAdmin, IsAgencyMember
from .models import Survey, Question, Response
from .serializers import SurveyReader, SurveyWriter, QuestionReader, QuestionWriter, ResponseReader, ResponseWriter


class SurveyViewset(ModelViewSet):
    queryset = Survey.objects.all()
    read_serializer_class = SurveyReader
    write_serializer_class = SurveyWriter
    permission_classes = [IsAdmin | IsAgencyMember]

    def get_queryset(self):
        return Survey.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class QuestionViewset(ModelViewSet):
    queryset = Question.objects.all()
    read_serializer_class = QuestionReader
    write_serializer_class = QuestionWriter
    permission_classes = [IsAdmin | IsAgencyMember]

    def get_queryset(self):
        return Question.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ResponseViewset(ModelViewSet):
    queryset = Response.objects.all()
    read_serializer_class = ResponseReader
    write_serializer_class = ResponseWriter
    permission_classes = [IsAdmin | IsAgencyMember]

    def get_queryset(self):
        return Response.objects.for_user(self.request.user)
