from rest_framework import serializers
from .models import Survey


class SurveyReader(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'name', 'definition', 'is_public',
                  'created_by', 'created_at', 'modified_at')


class SurveyWriter(SurveyReader):
    pass
