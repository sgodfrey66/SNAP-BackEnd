from django.db import models
from core.models import ObjectRoot
from client.models import Client


class Agency(ObjectRoot):
    class Meta:
        db_table = 'agency'
        verbose_name_plural = 'Agencies'
        ordering = ['name']

    name = models.CharField(max_length=64)

    # Reference field for internal cross-reference
    ref_id = models.IntegerField(unique=True, null=True)

    eligibility = models.ManyToManyField(
        'eligibility.Eligibility', related_name='eligibility', through='eligibility.AgencyEligibilityConfig')

    # security_groups = models.ManyToManyField(
    #     'security.SecurityGroup', related_name='agencies', through='security.SecurityGroupAgencyConfig'
    # )

    def __str__(self):
        return self.name


class AgencyClient(models.Model):
    class Meta:
        db_table = 'agency_client'

    client = models.ForeignKey(Client, related_name='agency_clients',
                               on_delete=models.PROTECT)
    agency_ref = models.ForeignKey(Agency, to_field='ref_id', db_column='agency_ref',
                                   null=True, on_delete=models.CASCADE)
    desc = models.CharField(max_length=125, null=True)
