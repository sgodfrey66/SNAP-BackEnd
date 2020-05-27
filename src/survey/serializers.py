from rest_framework import serializers
from core.serializers import ContentObjectRelatedField, ObjectSerializer, CreatedByReader
from .models import Survey, Question, Response, Answer


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
        fields = ('id', 'object', 'title', 'description', 'category', 'options', 'other', 'refusable', 'is_public',
                  'created_by', 'created_at', 'modified_at')


class QuestionWriter(QuestionReader):
    pass


class AnswerWriter(ObjectSerializer):
    #    response = serializers.ReadOnlyField()

    class Meta:
        model = Answer
        fields = ('question', 'value')


class ResponseReader(ObjectSerializer):
    created_by = CreatedByReader(read_only=True)
    respondent = ContentObjectRelatedField(read_only=True)

    class Meta:
        model = Response
        fields = ('id', 'object', 'respondent', 'created_by', 'created_at', 'modified_at')


class ResponseWriter(ObjectSerializer):
    class RespondentWriter(ContentObjectRelatedField):
        def get_queryset(self):
            print(('get_qs'))
            return None

    answers = AnswerWriter(many=True)
    respondent = RespondentWriter()

    class Meta:
        model = Response
        fields = ('survey', 'respondent', 'answers')

    def create(self, validated_data):
        # TODO: check access permissions to survey, questions, respondent
        response = Response.objects.create(
            survey=validated_data['survey'],
            respondent=validated_data['respondent'],
            created_by=validated_data['created_by'],
        )
        for ans in validated_data['answers']:
            Answer.objects.create(response=response, **ans)

        return response
