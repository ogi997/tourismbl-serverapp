from rest_framework import generics, permissions
from exif import Image
from django.contrib.gis.geos import Point
from .models import Location
from choices.models import Visibility
from .serializers import (LocationSerializer, LocationListSerializer, LocationForIDSerializer, LocationUpdateSerializer,
                          LocationDeleteSerializer)
from django.db.models import Q
from users.permissions import IsAdminUser
from locationUpdateRequest.models import LocationUpdateRequest
from utils.Coordinates import Coordinates


class LocationCreateAPIView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def perform_create(self, serializer):
        with self.request.data['image'] as src:
            coords = Coordinates.image_coordinates(self, Image(src.read()))
            serializer.save(last_user=self.request.user, geometry=Point(coords))


class LocationByIDAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Location.objects.all()
    serializer_class = LocationForIDSerializer


class LocationByCategory(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LocationListSerializer

    def get_queryset(self):
        user = self.request.user
        category = self.request.query_params.get('category', "ALL")
        if user.is_authenticated:
            if category == "ALL":
                return Location.objects.filter(
                    Q(visibility=Visibility.PUBLIC, active=True) |
                    Q(visibility=Visibility.ONLY_ME, last_user=user) |
                    Q(visibility=Visibility.LOGGED_USER, active=True)
                )
            return Location.objects.filter(
                Q(visibility=Visibility.PUBLIC, active=True, category=category) |
                Q(visibility=Visibility.ONLY_ME, last_user=user, category=category) |
                Q(visibility=Visibility.LOGGED_USER, active=True, category=category)
            )
        else:
            if category == "ALL":
                return Location.objects.filter(visibility=Visibility.PUBLIC, active=True)
            return Location.objects.filter(visibility=Visibility.PUBLIC, active=True, category=category)


class LocationUpdateByIdAPIView(generics.UpdateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = Location.objects.all()
    serializer_class = LocationUpdateSerializer

    def get_object(self):
        return LocationUpdateRequest.objects.get(id_update=self.kwargs['pk'])


class LocationDeleteByIdAPIView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Location.objects.all()
    serializer_class = LocationDeleteSerializer
