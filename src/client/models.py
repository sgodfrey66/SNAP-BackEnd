from django.db import models
from core.models import ObjectRoot


class ClientManager(models.Manager):
    def for_user(self, user):
        return super().get_queryset().filter(agency_clients__agency=user.profile.agency)


class Client(ObjectRoot):
    class Meta:
        db_table = 'client'
        # permissions = [
        #     ("view", "Can change the status of tasks"),
        # ]
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, default='', blank=True)
    last_name = models.CharField(max_length=64)
    dob = models.DateField()

    objects = ClientManager()

    @property
    def full_name(self):
        parts = [self.first_name, self.middle_name, self.last_name]
        return ' '.join([p for p in parts if p])

    def __str__(self):
        return self.full_name
