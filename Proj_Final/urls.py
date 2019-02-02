from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('website.urls')),
    path('sistema/', include('core.urls')),
    path('admin/', admin.site.urls),
]
