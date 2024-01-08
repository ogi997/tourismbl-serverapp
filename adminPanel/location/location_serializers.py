from rest_framework import serializers
from locations.models import Location
from locationUpdateRequest.models import LocationUpdateRequest
from utils.Coordinates import Coordinates
from exif import Image
from django.contrib.gis.geos import Point


class GetAllLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "title", "description"]


class GetLocationByIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "title", "description", "category", "image", "last_user", "active"]


class BlockLocationByIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "active")

    def update(self, instance, validated_data):
        instance.active = not instance.active
        instance.save()

        return instance


class DeleteLocationByIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location


class LocationUpdateSerializer(serializers.Serializer):
    class Meta:
        model = Location
        # fields = "__all__"

    def update(self, instance, validated_data):
        old_data = Location.objects.get(id=instance.id_update)
        old_data.title = instance.title
        old_data.description = instance.description
        old_data.category = instance.category
        old_data.image = instance.image

        with instance.image as src:
            old_data.geometry = Point(Coordinates.image_coordinates(self, Image(src.read())))
        old_data.visibility = instance.visibility
        old_data.save()
        return old_data
    # def update(self, instance, validated_data):
    #     # instance.save()
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.description = validated_data.get("description", instance.description)
    #     instance.category = validated_data.get("category", instance.category)
    #     instance.visibility = validated_data.get("visibility", instance.visibility)
    #     instance.image = validated_data.get("image", instance.image)
    #     #print(instance.title)
    #     #print(validated_data.get("title", instance.title))
    #     #instance.save()
    #     return instance


class DeleteLocationUpdateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationUpdateRequest
