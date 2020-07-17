from model_utils.managers import SoftDeletableManager


class EligibilityObjectManager(SoftDeletableManager):
    def for_user(self, user):
        if user.is_superuser:
            return super().get_queryset()
        if not hasattr(user, 'profile'):
            return self.none()

        return user.profile.agency.eligibility.all()


class AgencyEligibilityConfigObjectManager(SoftDeletableManager):
    def for_user(self, user):
        if user.is_superuser:
            return super().get_queryset()
        if not hasattr(user, 'profile'):
            return self.none()

        # return all configs where config.agency == user's agency
        return super().get_queryset().filter(agency=user.profile.agency)


class ClientEligibilityObjectManager(AgencyEligibilityConfigObjectManager):
    def for_user(self, user):
        if user.is_superuser:
            return super().get_queryset()
        if not hasattr(user, 'profile'):
            return self.none()

        # return all elibilities where client agency == user's agency
        return super().get_queryset().filter(
            client__created_by__profile__agency=user.profile.agency
        )
