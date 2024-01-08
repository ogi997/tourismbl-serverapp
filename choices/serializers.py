from rest_framework import serializers


class ModelSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4)
    name = serializers.CharField(max_length=25)

    class Meta:
        fields = ('code', 'name')
