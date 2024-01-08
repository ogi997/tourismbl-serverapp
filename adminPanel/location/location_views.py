from rest_framework import generics
from locations.models import Location
from locationUpdateRequest.models import LocationUpdateRequest
from users.permissions import IsAdminUser
from .location_serializers import (GetAllLocationSerializer, GetLocationByIdSerializer, BlockLocationByIdSerializer,
                                   DeleteLocationByIdSerializer, LocationUpdateSerializer,
                                   DeleteLocationUpdateRequestSerializer)


class GetAllLocationsAPIView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Location.objects.all()
    serializer_class = GetAllLocationSerializer


class GetLocationByIdAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Location.objects.all()
    serializer_class = GetLocationByIdSerializer


class BlockLocationByIdAPIView(generics.UpdateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Location.objects.all()
    serializer_class = BlockLocationByIdSerializer


class DeleteLocationByIdAPIView(generics.DestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Location.objects.all()
    serializer_class = DeleteLocationByIdSerializer


class LocationUpdateByIdAPIView(generics.UpdateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = Location.objects.all()
    serializer_class = LocationUpdateSerializer

    def get_object(self):
        return LocationUpdateRequest.objects.get(id_update=self.kwargs['pk'])


class DeleteLocationUpdateReqeustAPIView(generics.DestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = LocationUpdateRequest.objects.all()
    serializer_class = DeleteLocationUpdateRequestSerializer
