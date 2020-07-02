import uuid
from django.db import models
from simple_history.models import HistoricalRecords
from agency.models import Agency
from client.models import Client
from core.models import ObjectRoot
from .enums import EligibilityStatus
from .managers import EligibilityObjectManager, AgencyEligibilityConfigObjectManager, ClientEligibilityObjectManager


class Eligibility(ObjectRoot):
    class Meta:
        verbose_name_plural = 'Eligibility'
        db_table = 'eligibility'

    name = models.CharField(max_length=64)
    objects = EligibilityObjectManager()


class AgencyEligibilityConfig(ObjectRoot):
    class Meta:
        db_table = 'eligibility_agency_config'

    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    eligibility = models.ForeignKey(Eligibility, on_delete=models.CASCADE)

    objects = AgencyEligibilityConfigObjectManager()


class ClientEligibility(ObjectRoot):
    class Meta:
        db_table = 'eligibility_client'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='eligibility')
    eligibility = models.ForeignKey(Eligibility, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=32,
        choices=[(x.name, x.value) for x in EligibilityStatus]
    )
    history = HistoricalRecords()

    objects = ClientEligibilityObjectManager()
