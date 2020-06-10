from django.db import models
from core.models import ObjectRoot
from client.models import Client
from program.models import Program


class Agency(ObjectRoot):
    class Meta:
        db_table = 'agency'
        verbose_name_plural = 'Agencies'
    name = models.CharField(max_length=64)
    programs = models.ManyToManyField(Program)

    def __str__(self):
        return self.name


class AgencyClient(models.Model):
    class Meta:
        db_table = 'agency_client'
    client = models.ForeignKey(
        Client, related_name='agency_clients', on_delete=models.PROTECT)
    agency = models.ForeignKey(
        Agency, related_name='agency_clients', on_delete=models.PROTECT)
