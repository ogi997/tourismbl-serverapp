from rest_framework import serializers
from users.models import User


class ToggleActiveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "is_active")

    def update(self, instance, validated_data):
        instance.is_active = not instance.is_active
        instance.save()

        return instance


class ToggleUserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "is_admin")

    def update(self, instance, validated_data):
        instance.is_admin = not instance.is_admin
        instance.save()

        return instance


class GetAllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "is_active", "is_admin"]


class UserSerializerForID(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email", "is_active", "is_admin", "avatar"]


class DeleteUserSerializerForID(serializers.ModelSerializer):
    class Meta:
        model = User
