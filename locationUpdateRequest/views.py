from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import LocationUpdateRequest
from .serializers import LocationUpdateRequestSerializer, CheckIfRequestExistSerializer
from exif import Image


class RequestUpdateLocationAPIView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = LocationUpdateRequest.objects.all()
    serializer_class = LocationUpdateRequestSerializer

    def perform_create(self, serializer):
        with self.request.data['image'] as src:
            if not Image(src.read()).has_exif:
                raise ValueError("Image does not contain exif data.")
            serializer.save(last_user=self.request.user)


class CheckIfRequestExistAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = LocationUpdateRequest.objects.all()
    serializer_class = CheckIfRequestExistSerializer

    def get(self, request, *args, **kwargs):
        return Response({"exist": LocationUpdateRequest.objects.filter(id_update=kwargs['pk']).exists()},
                        status.HTTP_200_OK)
