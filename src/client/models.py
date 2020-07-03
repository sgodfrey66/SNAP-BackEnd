from django.db import models
from core.models import ObjectRoot
from core.managers import AgencyObjectManager


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

    objects = AgencyObjectManager()

    @property
    def full_name(self):
        parts = [self.first_name, self.middle_name, self.last_name]
        return ' '.join([p for p in parts if p])

    def __str__(self):
        return self.full_name
