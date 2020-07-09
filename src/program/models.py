import uuid
from django.db import models
from simple_history.models import HistoricalRecords
from core.models import ObjectRoot
from agency.models import Agency
from client.models import Client
from survey.models import Survey, Response
from .enums import EnrollmentStatus, ProgramEligibilityStatus
from .managers import (
    ProgramObjectManager, AgencyProgramConfigObjectManager,
    ProgramEligibilityObjectManager, EnrollmentObjectManager,
)


class Program(ObjectRoot):
    class Meta:
        db_table = 'program'
        ordering = ['name']

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
    class Meta:
        ordering = ['-created_at']

    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    agency_enrollment_entry_survey = models.ForeignKey(
        Survey, related_name='agency_programs_where_is_entry_survey', null=True, blank=True, on_delete=models.SET_NULL)
    agency_enrollment_update_survey = models.ForeignKey(
        Survey, related_name='agency_programs_where_is_update_survey', null=True, blank=True, on_delete=models.SET_NULL)
    agency_enrollment_exit_survey = models.ForeignKey(
        Survey, related_name='agency_programs_where_is_exit_survey', null=True, blank=True, on_delete=models.SET_NULL)

    objects = AgencyProgramConfigObjectManager()

    @property
    def enrollment_entry_survey(self):
        return self.agency_enrollment_entry_survey or self.program.enrollment_entry_survey

    @property
    def enrollment_update_survey(self):
        return self.agency_enrollment_update_survey or self.program.enrollment_update_survey

    @property
    def enrollment_exit_survey(self):
        return self.agency_enrollment_exit_survey or self.program.enrollment_exit_survey

    def __str__(self):
        return f"{self.program.name}@{self.agency.name}"


class Enrollment(ObjectRoot):
    class Meta:
        ordering = ['-created_at']

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='enrollments')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='enrollments')
    status = models.CharField(
        max_length=32,
        choices=[(x.name, x.value) for x in EnrollmentStatus]
    )
    response = models.ForeignKey(Response, on_delete=models.SET_NULL,
                                 related_name='enrollment', blank=True, null=True)
    history = HistoricalRecords()

    objects = EnrollmentObjectManager()

    def __str__(self):
        return f"{self.id}"


class ProgramEligibility(ObjectRoot):
    class Meta:
        verbose_name_plural = 'Program eligibility'
        ordering = ['-created_at']

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='program_eligibility')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='program_eligibility')
    status = models.CharField(
        max_length=32,
        choices=[(x.name, x.value) for x in ProgramEligibilityStatus]
    )
    history = HistoricalRecords()

    objects = ProgramEligibilityObjectManager()
