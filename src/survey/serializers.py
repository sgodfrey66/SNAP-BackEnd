from core.serializers import ContentObjectRelatedField, ObjectSerializer, CreatedByReader
from .models import Survey, Question, Response


class SurveyReader(ObjectSerializer):
    created_by = CreatedByReader(read_only=True)

    class Meta:
        model = Survey
        fields = ('id', 'object', 'name', 'definition', 'is_public',
                  'created_by', 'created_at', 'modified_at')


class SurveyWriter(SurveyReader):
    pass


class QuestionReader(ObjectSerializer):
    created_by = CreatedByReader(read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'object', 'title', 'description', 'category', 'is_public',
                  'created_by', 'created_at', 'modified_at')


class QuestionWriter(QuestionReader):
    pass


class ResponseReader(ObjectSerializer):
    created_by = CreatedByReader(read_only=True)
    respondent = ContentObjectRelatedField(read_only=True)

    class Meta:
        model = Response
        fields = ('id', 'object', 'respondent', 'created_by', 'created_at', 'modified_at')


class ResponseWriter(ResponseReader):
    pass
