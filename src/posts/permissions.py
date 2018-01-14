from rest_framework.permissions import BasePermission


class PostPermissions(BasePermission):

    def has_permission(self, request, view):
        from posts.api import PostCreateAPI

        if request.method == 'GET' and view.get_queryset() is not None and len(view.get_queryset()) != 0:
            return True

        if request.method == 'PUT' or request.method == 'DELETE':
            return request.user.is_superuser or view.get_queryset()[0].user == request.user

        return request.user.is_authenticated and request.method == 'POST' and isinstance(view, PostCreateAPI)
