from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import JSONField, ArrayField
from django.db.models.signals import pre_save
from django.dispatch import receiver

from core.models import ObjectRoot
from core.managers import AgencyObjectManager
from core.json_yaml_field import JsonYamlField
from survey.enums import QuestionCategory


class Survey(ObjectRoot):
    class Meta:
        db_table = 'survey'
        ordering = ['created_at']
    name = models.CharField(max_length=64)
    definition = JsonYamlField()
    questions = ArrayField(models.UUIDField(), null=True, blank=True)
    is_public = models.BooleanField(default=False)

    objects = AgencyObjectManager()

    def __str__(self):
        return self.name


class Question(ObjectRoot):
    title = models.CharField(max_length=64)
    description = models.TextField(default='', blank=True)
    category = models.CharField(choices=QuestionCategory.choices,
                                max_length=32, default=QuestionCategory.TEXT)
    options = ArrayField(models.CharField(
        max_length=64), null=True, blank=True)
    other = models.BooleanField(default=False)
    refusable = models.BooleanField(default=False)
    rows = models.IntegerField(null=True, blank=True)
    columns = JSONField(null=True, blank=True)
    is_public = models.BooleanField(default=False)

    objects = AgencyObjectManager()

    def __str__(self):
        return self.title


class Response(ObjectRoot):
    respondent_type = models.ForeignKey(ContentType, null=True, related_name='responses', on_delete=models.PROTECT)
    respondent_id = models.UUIDField(primary_key=False)
    respondent = GenericForeignKey('respondent_type', 'respondent_id')
    survey = models.ForeignKey(
        Survey, related_name='responses', on_delete=models.PROTECT
    )

    objects = AgencyObjectManager()


class Answer(models.Model):
    response = models.ForeignKey(
        Response, related_name='answers', on_delete=models.PROTECT
    )
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.PROTECT
    )
    value = models.CharField(max_length=256)


@receiver(pre_save, sender=Survey)
def save_related_questions(sender, instance, *args, **kwargs):

    def traverse_items(current, question_ids = []):
        if current.get('type', None) == 'question' and 'question_id' in current:
            question_ids.append(current['question_id'])

        for item in current.get('items', []):
            traverse_items(item, question_ids)

        return question_ids

    instance.questions = traverse_items(instance.definition)
