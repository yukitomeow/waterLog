from django.urls import path, re_path, include
from water.views import top
from accounts.views import redirect_to_user_profile

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import redirect_to_language

urlpatterns = [
    path("", redirect_to_language, name="redirect_to_language"),  # Add this line
    path("admin/", admin.site.urls),
    re_path(r'^(?P<language_code>en|ja)/$', top, name="top"),
    re_path(r'^(?P<language_code>en|ja)/water/', include("water.urls")),
    re_path(r'^(?P<language_code>en|ja)/accounts/', include("accounts.urls")),
    path('i18n/', include('django.conf.urls.i18n')),
]

# Only serve static files this way in a development environment!
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



