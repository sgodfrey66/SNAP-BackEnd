import uuid
from django.db import models
from simple_history.models import HistoricalRecords
from core.models import ObjectRoot
from agency.models import Agency
from client.models import Client
from survey.models import Survey, Response
from .enums import EnrollmentStatus, EligibilityStatus
from .managers import ProgramObjectManager


class Program(ObjectRoot):
    class Meta:
        db_table = 'program'

    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, default='')

    enrollment_entry_survey = models.ForeignKey(
        Survey, related_name='programs_where_is_entry_survey', null=True, blank=True, on_delete=models.SET_NULL)
    enrollment_update_survey = models.ForeignKey(
        Survey, related_name='programs_where_is_update_survey', null=True, blank=True, on_delete=models.SET_NULL)
    enrollment_exit_survey = models.ForeignKey(
        Survey, related_name='programs_where_is_exit_survey', null=True, blank=True, on_delete=models.SET_NULL)

    objects = ProgramObjectManager()

    def __str__(self):
        return self.name


class AgencyProgramConfig(ObjectRoot):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    enrollment_entry_survey = models.ForeignKey(
        Survey, related_name='agency_programs_where_is_entry_survey', null=True, blank=True, on_delete=models.SET_NULL)
    enrollment_update_survey = models.ForeignKey(
        Survey, related_name='agency_programs_where_is_update_survey', null=True, blank=True, on_delete=models.SET_NULL)
    enrollment_exit_survey = models.ForeignKey(
        Survey, related_name='agency_programs_where_is_exit_survey', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.program.name}@{self.agency.name}"


class Enrollment(ObjectRoot):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='enrollments')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='enrollments')
    status = models.CharField(
        max_length=32,
        choices=[(x.name, x.value) for x in EnrollmentStatus]
    )
    response = models.ForeignKey(Response, on_delete=models.SET_NULL,
                                 related_name='enrollment', blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.id}"


class Eligibility(ObjectRoot):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    status = models.CharField(
        max_length=32,
        choices=[(x.name, x.value) for x in EligibilityStatus]
    )
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='eligibility')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='eligibility')
    history = HistoricalRecords()
