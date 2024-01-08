from django.urls import path
from .location_update_views import (GetAllLocationUpdateRequestAPIView, GetUpdateLocationRequestAPIView,
                                    DeleteUpdateLocationRequestAPIView)

urlpatterns = [
    path("get-all-location-requests/", GetAllLocationUpdateRequestAPIView.as_view(), name="get_all_location_updates"),
    path("get-update-location-request/<int:pk>", GetUpdateLocationRequestAPIView.as_view(),
         name="get_update_location_request"),
    path("delete-update-location-request/<int:pk>", DeleteUpdateLocationRequestAPIView.as_view(),
         name="delete_update_location_request"),
]
