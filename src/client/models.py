from django.db import models
from core.models import ObjectRoot
from core.managers import AgencyObjectManager
from django.core.validators import validate_comma_separated_integer_list



class Client(ObjectRoot):
    class Meta:
        db_table = 'client'
        ordering = ['-created_at']
        # permissions = [
        #     ("view", "Can change the status of tasks"),
        # ]
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, default='', blank=True)
    last_name = models.CharField(max_length=64)
    dob = models.DateField()

    # Agency associations for this client
    agency_assoc = models.CharField(validators=[validate_comma_separated_integer_list],
                                   max_length=200, blank=True, null=True, default='')


    objects = AgencyObjectManager()

    @property
    def full_name(self):
        parts = [self.first_name, self.middle_name, self.last_name]
        return ' '.join([p for p in parts if p])

    def __str__(self):
        return self.full_name
