from rest_framework import generics, permissions
from .models import User
from .serializers import (UserSerializer, UserIdentitySerializer, ChangeUserDataSerializer,
                          ChangeUserPasswordSerializer, ChangeUserAvatarSerializer)


class UserCreateView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserIdentityAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserIdentitySerializer

    def get_object(self):
        return self.request.user


class ChangeUserAvatarAPIView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = ChangeUserAvatarSerializer

    def get_object(self):
        return self.request.user


class UserChangeDataAPIView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = ChangeUserDataSerializer

    def get_object(self):
        return self.request.user


class ChangeUserPasswordAPIView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = ChangeUserPasswordSerializer

    def get_object(self):
        return self.request.user
