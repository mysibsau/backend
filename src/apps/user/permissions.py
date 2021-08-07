from rest_framework.permissions import BasePermission


class IsStudentAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request, 'student')
