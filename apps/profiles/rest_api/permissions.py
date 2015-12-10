from rest_framework.permissions import BasePermission


class IsEventManagers(BasePermission):
    """
    Allows access only to Event Managers
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_event_manager