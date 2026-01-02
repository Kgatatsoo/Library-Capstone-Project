from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LibrarySystemapp.urls')),      # home page /
    path('api/', include('LibrarySystemapp.urls')),  # /api/
]
