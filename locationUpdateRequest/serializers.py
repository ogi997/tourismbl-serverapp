from rest_framework import serializers
from .models import LocationUpdateRequest


class LocationUpdateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationUpdateRequest
        fields = ("title", "description", "image", "category", "visibility", "id_update")


class CheckIfRequestExistSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationUpdateRequest
