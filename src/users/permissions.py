from rest_framework.permissions import BasePermission


class UserPermissions(BasePermission):

    def has_permission(self, request, view):
        from users.api import UserDetailAPI

        if request.method == 'POST' or request.user.is_superuser:
            return True

        if request.user.is_authenticated and request.method == 'GET' and isinstance(view, UserDetailAPI):
            return True

        return request.user.is_authenticated and (request.method == 'PUT' or request.method == 'DELETE')

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_superuser
