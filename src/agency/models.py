from django.db import models
from core.models import PrimaryModel
from client.models import Client


class Agency(PrimaryModel):
    class Meta:
        db_table = 'agency'
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class AgencyClient(models.Model):
    class Meta:
        db_table = 'agency_client'
    client = models.ForeignKey(
        Client, related_name='agency_clients', on_delete=models.PROTECT)
    agency = models.ForeignKey(
        Agency, related_name='agency_clients', on_delete=models.PROTECT)
