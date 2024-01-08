from django.urls import path
from .views import VisibilityListView, CategoryListView

urlpatterns = [
    path("visibility-list/", VisibilityListView.as_view(), name="visibility_list"),
    path("category-list/", CategoryListView.as_view(), name="categories_list"),
]
