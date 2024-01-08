from rest_framework import serializers
from locationUpdateRequest.models import LocationUpdateRequest


class GetAllLocationUpdateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationUpdateRequest
        fields = '__all__'


class GetLocationUpdateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationUpdateRequest
        fields = '__all__'


class DeleteLocationUpdateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationUpdateRequest
