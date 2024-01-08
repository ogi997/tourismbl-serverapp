from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email", "password", "avatar"]

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        user.save()
        return user


class UserIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", "first_name", "last_name", "username", "email", "date_joined", "is_staff",
            "is_active", "is_admin", "avatar"
        )
        read_only_fields = (
            "first_name", "last_name", "email", "username", "date_joined", "is_staff",
            "is_active", "is_admin", "avatar"
        )


class ChangeUserAvatarSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(write_only=True)

    class Meta:
        model = User
        fields = ("avatar",)
        read_only_fields = ("avatar",)

    def update(self, instance, validated_data):
        print(instance.avatar)
        print(validated_data['avatar'])
        instance.avatar = validated_data['avatar']
        instance.save()

        return instance


# UPDATE USER-A potrebno je promjeniti dodati avatar itd.
class ChangeUserDataSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    # avatar = serializers.ImageField(write_only=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        read_only_fields = ("first_name", "last_name", "email")

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        # instance.avatar = validated_data['avatar']
        instance.save()
        return instance


class ChangeUserPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_repeat = serializers.CharField(write_only=True, required=True)
    password_old = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("password", "password_repeat", "password_old")

    def validate_old_password(self, value):
        user = self.context['request'].user
        err_msg = "Wrong old password."
        if not user.check_password(value):
            raise serializers.ValidationError(err_msg)
        return True

    def validate(self, data):
        err_msg1 = "Password didn't match."
        err_msg2 = "Please enter different new password."

        if data['password'] != data['password_repeat']:
            raise serializers.ValidationError(err_msg1)
        elif data['password'] == data['password_old']:
            raise serializers.ValidationError(err_msg2)
        else:
            if self.validate_old_password(data['password_old']):
                return data

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data['password'])
        instance.save()
        return instance
