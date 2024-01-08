from django.urls import path
from .user_views import (ToggleActiveUserAccountAPIView, ToggleUserAdminAPIView, GetAllUsersAPIView, GetUserByIdAPIView, DeleteUserByIdAPIView)

urlpatterns = [
    path("toggle-active-user/<int:pk>", ToggleActiveUserAccountAPIView.as_view(), name="toggle_active_user"),
    path("toggle-admin-user/<int:pk>", ToggleUserAdminAPIView.as_view(), name="toggle_admin_user"),
    path("get-all-users/", GetAllUsersAPIView.as_view(), name="get_all_users"),
    path("get-user/<int:pk>", GetUserByIdAPIView.as_view(), name="get_user_by_id"),
    path("delete-user/<int:pk>", DeleteUserByIdAPIView.as_view(), name="delete_user_by_id"),
]
