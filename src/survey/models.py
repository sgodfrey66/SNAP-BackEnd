from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from core.models import PrimaryModel
from core.fields import EnumCharField
from client.models import Client
from survey.enums import QuestionCategory


class Survey(PrimaryModel):
    class Meta:
        db_table = 'survey'
    name = models.CharField(max_length=64)
    definition = JSONField()

    def __str__(self):
        return self.name


class Question(PrimaryModel):
    title = models.CharField(max_length=64)
    description = models.TextField()
    category = EnumCharField(enum=QuestionCategory,
                             max_length=32, default=QuestionCategory.TEXT)
    options = ArrayField(models.CharField(max_length=64, blank=True))
    other = models.BooleanField()
    refusable = models.BooleanField()
    rows = models.IntegerField()
    columns = JSONField()
    public = models.BooleanField()

    def __str__(self):
        return self.title


class Response(PrimaryModel):
    client = models.ForeignKey(
        Client, related_name='responses', on_delete=models.PROTECT
    )
    survey = models.ForeignKey(
        Survey, related_name='responses', on_delete=models.PROTECT
    )


class Answer(PrimaryModel):
    response = models.ForeignKey(
        Response, related_name='answers', on_delete=models.PROTECT
    )
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.PROTECT
    )
