from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from users.permissions import UserPermissions
from users.serializers import UserSerializer, UsersSerializer


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
