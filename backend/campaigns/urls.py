from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, usd_to_inr_rate
from .views import dashboard


router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet, basename='campaign')

urlpatterns = [
    path('exchange-rate/', usd_to_inr_rate),
    path('dashboard/', dashboard),
]

urlpatterns += router.urls
