from rest_framework.permissions import IsAuthenticated


class IsAgencyMember(IsAuthenticated):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view=None):
        try:
            return bool(request.user.profile.agency)
        except AttributeError:
            pass
        return False


class IsAdmin(IsAuthenticated):
    """
    Allows access only to admins.
    """

    def has_permission(self, request, view=None):
        try:
            return request.user.is_superuser
        except AttributeError:
            pass
        return False


class IsOwner(IsAuthenticated):
    """
    Checks if created_by is the same as the user
    """

    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user
