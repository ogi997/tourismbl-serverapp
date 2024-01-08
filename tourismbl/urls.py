from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("users.urls")),
    path("choices/", include("choices.urls")),
    path("admin-panel/user/", include("adminPanel.user.user_urls")),
    path("admin-panel/location/", include("adminPanel.location.location_urls")),
    path("admin-panel/update-location/", include("adminPanel.locationUpdate.location_update_urls")),
    path("locations/", include("locations.urls")),
    path("location-update/", include("locationUpdateRequest.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
