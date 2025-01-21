from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from log.views import DeviceInfoView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("user.urls")),
    path("profile/", include("profiles.urls")),
    path("log/device-info/", DeviceInfoView.as_view(), name="device-info"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
