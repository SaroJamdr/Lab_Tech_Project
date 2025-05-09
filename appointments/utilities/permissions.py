from rest_framework.permissions import BasePermission

class AppointmentPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True  # Anyone can create

        return request.user and request.user.is_authenticated and request.user.is_superuser