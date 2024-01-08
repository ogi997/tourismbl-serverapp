from rest_framework import generics
from users.permissions import IsAdminUser
from locationUpdateRequest.models import LocationUpdateRequest
from .location_update_serializer import (GetAllLocationUpdateRequestSerializer, GetLocationUpdateRequestSerializer,
                                         DeleteLocationUpdateRequestSerializer)


class GetAllLocationUpdateRequestAPIView(generics.ListAPIView):
    permission_classes = (IsAdminUser, )
    queryset = LocationUpdateRequest.objects.all()
    serializer_class = GetAllLocationUpdateRequestSerializer


class GetUpdateLocationRequestAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAdminUser,)
    queryset = LocationUpdateRequest.objects.all()
    serializer_class = GetLocationUpdateRequestSerializer


class DeleteUpdateLocationRequestAPIView(generics.DestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = LocationUpdateRequest.objects.all()
    serializer_class = DeleteLocationUpdateRequestSerializer
