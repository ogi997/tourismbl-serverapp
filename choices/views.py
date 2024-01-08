from rest_framework import generics, permissions
from .models import Visibility, Categories
from .serializers import ModelSerializer


class ModelListAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ModelSerializer


class VisibilityListView(ModelListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = [{"code": item[0], "name": item[1]} for item in Visibility.choices]


class CategoryListView(ModelListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = [{"code": item[0], "name": item[1]} for item in Categories.choices]
