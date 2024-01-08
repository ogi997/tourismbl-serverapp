from django.urls import path
from .views import (LocationCreateAPIView, LocationByIDAPIView, LocationByCategory, LocationUpdateByIdAPIView,
                    LocationDeleteByIdAPIView)

urlpatterns = [
    path('location-create/', LocationCreateAPIView.as_view(), name="location_create"),
    path('get-all-locations-by-category/', LocationByCategory.as_view(), name="get_all_locations_by_category"),
    path('get-location/<int:pk>', LocationByIDAPIView.as_view(), name="get_location"),
    path('update/<int:pk>', LocationUpdateByIdAPIView.as_view(), name="update_location"),
    path('delete/<int:pk>', LocationDeleteByIdAPIView.as_view(), name="delete_location"),
]
