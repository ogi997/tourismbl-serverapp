from django.urls import path
from .views import RequestUpdateLocationAPIView, CheckIfRequestExistAPIView

urlpatterns = [
    path("request/", RequestUpdateLocationAPIView.as_view(), name="request_update_location"),
    path("check-if-request-exist/<int:pk>", CheckIfRequestExistAPIView.as_view(), name="check_if_request_exist"),
]
