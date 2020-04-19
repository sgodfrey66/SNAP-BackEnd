from django.db import models
from core.models import PrimaryModel


class Client(PrimaryModel):
    class Meta:
        db_table = 'client'
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, default='')
    last_name = models.CharField(max_length=64)
    dob = models.DateField()

    @property
    def full_name(self):
        parts = [self.first_name, self.middle_name, self.last_name]
        return ' '.join([p for p in parts if p])

    def __str__(self):
        return self.full_name
