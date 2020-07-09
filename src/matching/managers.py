from django.db import models


class MatchingConfigObjectManager(models.Manager):
    def for_user(self, user):
        if user.is_superuser:
            return super().get_queryset()
        if not hasattr(user, 'profile'):
            return self.none()

        return super().get_queryset().filter(agency=user.profile.agency)


class ClientMatchingObjectManager(models.Manager):
    def for_user(self, user):
        if user.is_superuser:
            return super().get_queryset()
        if not hasattr(user, 'profile'):
            return self.none()

        return super().get_queryset().filter(client__created_by__profile__agency=user.profile.agency)
