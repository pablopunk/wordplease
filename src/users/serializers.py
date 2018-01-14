from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UsersSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):
        pass


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
