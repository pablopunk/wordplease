from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    abstract = models.CharField(max_length=500)
    body = models.TextField()
    image = models.URLField(blank=True)
    published_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
