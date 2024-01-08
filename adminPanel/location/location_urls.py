from django.urls import path
from .location_views import (GetAllLocationsAPIView, GetLocationByIdAPIView, BlockLocationByIdAPIView,
                             DeleteLocationByIdAPIView, LocationUpdateByIdAPIView, DeleteLocationUpdateReqeustAPIView)


urlpatterns = [
    path("get-all-locations/", GetAllLocationsAPIView.as_view(), name="get_all_locations"),
    path("get-location/<int:pk>", GetLocationByIdAPIView.as_view(), name="get_location_by_id"),
    path("toggle-active-location/<int:pk>", BlockLocationByIdAPIView.as_view(), name="block_location"),
    path("delete-location/<int:pk>", DeleteLocationByIdAPIView.as_view(), name="delete_location"),
    path('update/<int:pk>', LocationUpdateByIdAPIView.as_view(), name="update_location"),
    path('delete-location-update-request/<int:pk>', DeleteLocationUpdateReqeustAPIView.as_view(),
         name="delete_location_update_request")
]
