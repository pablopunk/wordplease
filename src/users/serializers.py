from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UsersSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class UserSerializer(UsersSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_username(self, data):
        if self.instance is None and User.objects.filter(username=data).exists():
            raise ValidationError("User already exists")
        if self.instance is not None and self.instance.username != data and User.objects.filter(username=data).exists():
            raise ValidationError("Wanted username is already in use")
        return data

    def create(self, validated_data):
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.username = validated_data.get("username")
        instance.email = validated_data.get("email")
        instance.set_password(validated_data.get("password"))
        instance.save()
        return instance


def get_blog_relative_url(self):
    return "/blogs/{0}".format(self.username)

def get_blog_name(self):
    return self.username

# Add methods to User class
User.add_to_class('get_blog_relative_url', get_blog_relative_url)
User.add_to_class('get_blog_name', get_blog_name)


class BlogsSerializer(serializers.ModelSerializer):
    name = serializers.URLField(source='get_blog_name')
    url = serializers.URLField(source='get_blog_relative_url')

    class Meta:
        model = User
        fields = ['name', 'url']
