from django.db import models
from django.contrib.auth.models import User
from core.models import ObjectRoot, TimeStampedModel
from core.json_yaml_field import JsonYamlField
from agency.models import Agency
from client.models import Client
from program.models import Program


class MatchingConfig(ObjectRoot):
    class Meta:
        db_table = 'matching_config'
        ordering = ['created_at']

    agency = models.ForeignKey(Agency, related_name='matching_configs', on_delete=models.CASCADE)
    config = JsonYamlField()


class ClientMatching(ObjectRoot):
    class Meta:
        db_table = 'client_matching'
        ordering = ['created_at']

    client = models.ForeignKey(Client, related_name='matching', on_delete=models.CASCADE)
    program = models.ForeignKey(Program, related_name='matching', on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    config = models.ForeignKey(MatchingConfig, related_name='client_matches', on_delete=models.PROTECT)
    step = models.CharField(max_length=256)
    outcome = models.CharField(max_length=256)


class ClientMatchingHistory(TimeStampedModel):
    class Meta:
        db_table = 'client_matching_history'
        ordering = ['created_at']

    client_matching = models.ForeignKey(ClientMatching, related_name='history', on_delete=models.CASCADE)
    step = models.CharField(max_length=256)
    outcome = models.CharField(max_length=256)


class ClientMatchingNote(TimeStampedModel):
    class Meta:
        db_table = 'client_matching_note'
        ordering = ['created_at']

    client_matching = models.ForeignKey(ClientMatching, related_name='notes', on_delete=models.CASCADE)
    step = models.CharField(max_length=256)
    note = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
