from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, usd_to_inr_rate
from .views import campaign_list
from .views import dashboard


router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet, basename='campaign')

urlpatterns = [
    path('exchange-rate/', usd_to_inr_rate),
    path("campaigns/", campaign_list),
    path('dashboard/', dashboard),
]

urlpatterns += router.urls
