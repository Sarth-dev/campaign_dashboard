from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', lambda request: JsonResponse({"status": "API running"})),
    path('admin/', admin.site.urls),
    path('api/', include('backend.campaigns.urls')),
]
