from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.permissions import IsAdminUser
from .user_serializers import (GetAllUsersSerializer, UserSerializerForID, DeleteUserSerializerForID,
                               ToggleActiveUserSerializer, ToggleUserAdminSerializer)


class ToggleActiveUserAccountAPIView(generics.UpdateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = ToggleActiveUserSerializer


class ToggleUserAdminAPIView(generics.UpdateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = ToggleUserAdminSerializer


class GetAllUsersAPIView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = GetAllUsersSerializer

    def get(self, request, *args, **kwargs):
        current_user = request.user
        data = User.objects.exclude(id=current_user.id)
        serializer = GetAllUsersSerializer(data, many=True)

        return Response({"users": serializer.data}, status=status.HTTP_200_OK)


class GetUserByIdAPIView(generics.RetrieveAPIView):
    permissions = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializerForID


class DeleteUserByIdAPIView(generics.DestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = DeleteUserSerializerForID

    # admin locations manipulation
