from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('catalogue', include('catalogue.urls')),
    path('basket', include('basket.urls')),
    path('user_profiles', include('user_profiles.urls')),
    path('user_settings', include('user_settings.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
