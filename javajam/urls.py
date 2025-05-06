from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # Needed for static files

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('', include('jobs.urls')),  # This line connects your jobs app URLs
]

# Serving static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
