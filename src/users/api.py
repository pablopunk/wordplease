from rest_framework.filters import OrderingFilter
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from users.permissions import UserPermissions
from users.serializers import UserSerializer, UsersSerializer, BlogsSerializer


class UsersListAPI(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [UserPermissions]

    def get_serializer_class(self):
        return UsersSerializer if self.request.method == 'GET' else UserSerializer


class UserDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissions]


class BlogsListAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = BlogsSerializer
    filter_backends = (OrderingFilter, )
    ordering = ('username', )

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('name', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset
