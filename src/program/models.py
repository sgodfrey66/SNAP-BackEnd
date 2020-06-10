from django.db import models
from core.models import ObjectRoot
from survey.models import Survey


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

    def __str__(self):
        return self.name


# class Eligibility

# class Enrollment(ObjectRoot):
#     pass
