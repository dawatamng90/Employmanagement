from django.contrib import admin
from django.urls import path, include
from .views import home, about, service  # Import only the required views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),  # Add a name for the home path if needed
    path('index/', home),
    path('about/', about, name="about"),  # Adding names for easier reference
    path('service/', service, name="service"),
    path("emp/", include('emp.urls'))
]

# Only add static file configuration if MEDIA_URL and MEDIA_ROOT are defined
if settings.MEDIA_URL and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 