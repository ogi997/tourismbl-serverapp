from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        # geo_field = "geometry"
        fields = ("title", "description", "image", "category", "visibility")


class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "title", "description", "image", "geometry")
        geo_field = "geometry"


class LocationForIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "title", "description", "image", "geometry", "category", "visibility", "last_user")
        geo_field = "geometry"


class LocationUpdateSerializer(serializers.Serializer):
    class Meta:
        model = Location
        # fields = '__all__'

    def update(self, instance, validated_data):
        instance.save()
        return instance


class LocationDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
