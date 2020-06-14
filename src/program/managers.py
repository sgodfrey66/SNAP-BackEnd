from django.db import models


class ProgramObjectManager(models.Manager):
    def for_user(self, user):
        if user.is_superuser:
            return super().get_queryset()
        if not hasattr(user, 'profile'):
            return self.none()

        return user.profile.agency.programs.order_by('created_at').all()
