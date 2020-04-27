from django.db import models


class AgencyObjectManager(models.Manager):
    def for_user(self, user):
        if not hasattr(user, 'profile'):
            return self.none()
        return super().get_queryset().filter(created_by__profile__agency=user.profile.agency)