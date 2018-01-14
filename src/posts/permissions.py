from rest_framework.permissions import BasePermission


class PostPermissions(BasePermission):

    def has_permission(self, request, view):
        from posts.api import PostCreateAPI

        if request.method == 'PUT' or request.method == 'DELETE':
            print(view)
            return request.user.is_superuser or view.queryset[0].user == request.user

        return request.user.is_authenticated and request.method == 'POST' and isinstance(view, PostCreateAPI)
