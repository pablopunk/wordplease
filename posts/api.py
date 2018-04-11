from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from posts.models import Post
from posts.permissions import PostPermissions
from posts.serializers import PostsSerializer


class PostsListAPI(ListAPIView):
    serializer_class = PostsSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'body',)
    ordering_fields = ('title', 'published_at',)
    ordering = ('-published_at',)

    def get_queryset(self):
        username = self.kwargs['username']
        users = User.objects.filter(username=username)
        if len(users) != 0:
            if self.request.user != users[0] and not self.request.user.is_superuser:
                return Post.objects.filter(user=users[0], published_at__isnull=False)
            return Post.objects.filter(user=users[0])
        else:
            raise Http404


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = PostsSerializer
    permission_classes = [PostPermissions]

    def get_queryset(self):
        pk = self.kwargs['pk']
        posts = Post.objects.filter(pk=pk)
        if len(posts) != 0:
            allow_drafts = self.request.user.is_superuser or self.request.user == posts[0].user
            if posts[0].published_at is None and allow_drafts:
                return posts
            if posts[0].published_at is not None:
                return posts
        else:
            raise Http404


class PostCreateAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [PostPermissions]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
