from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
from posts.models import Post


def home(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by("-published_at")
    return render(request, "home.html", {'posts': posts[:10]})

def user_posts(request, username):
    try:
        user = User.objects.get(username=username).order_by("-published_at")
        posts = Post.objects.filter(user=user)
        return render(request, "blog.html", {'username': username,'posts': posts})
    except:
        return render(request, "404.html")

@login_required
def my_blog(request):
    drafts = Post.objects.filter(user=request.user, published_at__isnull=True)
    posts = Post.objects.filter(user=request.user, published_at__isnull=False).order_by("-published_at")
    posts = list(drafts) + list(posts) # concatenate. drafts first
    return render(request, "blog.html", {'username': request.user.username, 'posts': posts})
