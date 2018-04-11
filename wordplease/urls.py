"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from posts.api import PostsListAPI, PostCreateAPI, PostDetailAPI
from posts.views import home, my_blog, user_posts, CreatePostView, post_detail
from users.api import UsersListAPI, UserDetailAPI, BlogsListAPI
from users.views import blogs, signup


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('login', auth_views.login, {'template_name': 'login.html'}, name="login"),
    path('logout', auth_views.logout, {'next_page': '/'}, name="logout"),
    path('signup', signup, name="signup"),

    path('my_blog', my_blog, name="my_blog"),
    path('blogs/<username>', user_posts, name="user_posts"),
    path('blogs', blogs, name="blogs"),
    path('new-post', CreatePostView.as_view(), name="new_post"),
    path('blogs/<username>/<int:pk>', post_detail, name="post_detail"),

    path('api/1.0/users', UsersListAPI.as_view(), name="api_users"),
    path('api/1.0/users/<int:pk>', UserDetailAPI.as_view(), name="api_user"),
    path('api/1.0/blogs', BlogsListAPI.as_view(), name="api_blogs"),
    path('api/1.0/blogs/<username>', PostsListAPI.as_view(), name="api_blog"),
    path('api/1.0/posts/create', PostCreateAPI.as_view(), name="api_post_create"),
    path('api/1.0/posts/<int:pk>', PostDetailAPI.as_view(), name="api_post"),
]
