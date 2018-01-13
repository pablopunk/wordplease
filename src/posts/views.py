from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from posts.forms import PostForm
from posts.models import Post


def get_user_posts(user, with_drafts=False):
    drafts = []
    if with_drafts:
        drafts = Post.objects.filter(user=user, published_at__isnull=True).order_by("-created_at")
    posts = Post.objects.filter(user=user, published_at__isnull=False).order_by("-published_at")
    posts = list(drafts) + list(posts)
    if posts is None:
        posts = []

    return posts


def home(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by("-published_at")
    return render(request, "home.html", {'posts': posts[:10]})


def user_posts(request, username):
    users = User.objects.filter(username=username)
    if len(users) == 0:
        return render(request, "404.html")

    show_drafts = False
    if users[0] == request.user:
        show_drafts = True

    posts = get_user_posts(users[0], with_drafts=show_drafts)
    return render(request, "blog.html", {'username': username, 'posts': posts})


@login_required
def my_blog(request):
    posts = get_user_posts(request.user, with_drafts=True)
    return render(request, "blog.html", {'username': request.user.username, 'posts': posts})


def post_detail(request, username, pk):
    users = User.objects.filter(username=username)
    if len(users) == 0:
        return render(request, "404.html")
    posts = Post.objects.filter(user=users[0], pk=pk)
    if len(posts) == 0:
        return render(request, "404.html")

    post = posts[0]
    if post.published_at is None and post.user != request.user:
        return render(request, "404.html") # user can't see other user's drafts

    if request.method == 'POST' and request.POST.get('publish') is not None and post.user == request.user:
        post.published_at = datetime.now()
        post.save()
        messages.success(request, 'The post has been published!')
    elif request.method == 'POST' and request.POST.get('delete') is not None and post.user == request.user:
        post.delete()
        messages.success(request, 'Deleted post')
        return redirect("my_blog")
    return render(request, "post.html", {'post': post, 'categories': posts[0].categories.all()})


class CreatePostView(LoginRequiredMixin, View):

    def get(self, request):
        form = PostForm()
        return render(request, "new_blog.html", {'form': form})

    def post(self, request):
        post = Post()
        post.user = request.user
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            print(request.POST)
            if request.POST.get('publish') is not None:
                post.published_at = datetime.now()
            post = form.save()
            form = PostForm()  # empty form
            message = 'New post created!'
            messages.success(request, message)
            return redirect("my_blog")
        return render(request, "new_blog.html", {'form': form})
