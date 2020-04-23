from rest_framework.permissions import IsAuthenticated


class IsAgencyMember(IsAuthenticated):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        try:
            return bool(request.user.profile.agency)
        except AttributeError:
            pass
        return False


class IsOwner(IsAuthenticated):
    """
    Checks if created_by is the same as the user
    """

    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user
