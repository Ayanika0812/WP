from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel
    path('', include('webapp.urls')),  # Includes URLs from the 'webapp' app
]
