from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from core.models import ObjectRoot
from core.json_yaml_field import JsonYamlField
from client.models import Client
from survey.enums import QuestionCategory


class SurveyManager(models.Manager):
    def for_user(self, user):
        return super().get_queryset().filter(created_by__profile__agency=user.profile.agency)


class Survey(ObjectRoot):
    class Meta:
        db_table = 'survey'
    name = models.CharField(max_length=64)
    definition = JsonYamlField()
    is_public = models.BooleanField(default=False)

    objects = SurveyManager()

    def __str__(self):
        return self.name


class Question(ObjectRoot):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    category = models.CharField(choices=QuestionCategory.choices,
                                max_length=32, default=QuestionCategory.TEXT)
    options = ArrayField(models.CharField(
        max_length=64), null=True, blank=True)
    other = models.BooleanField()
    refusable = models.BooleanField()
    rows = models.IntegerField(null=True, blank=True)
    columns = JSONField(null=True, blank=True)
    public = models.BooleanField()

    def __str__(self):
        return self.title


class Response(ObjectRoot):
    client = models.ForeignKey(
        Client, related_name='responses', on_delete=models.PROTECT
    )
    survey = models.ForeignKey(
        Survey, related_name='responses', on_delete=models.PROTECT
    )


class Answer(models.Model):
    response = models.ForeignKey(
        Response, related_name='answers', on_delete=models.PROTECT
    )
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.PROTECT
    )
    value = models.CharField(max_length=256)
