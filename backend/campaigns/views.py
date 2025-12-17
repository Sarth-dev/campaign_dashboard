import requests
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Campaign
from rest_framework.viewsets import ModelViewSet
from .serializers import CampaignSerializer
# Create your views here.



def dashboard(request):
    campaigns = Campaign.objects.all()

    platform_data = {}
    for campaign in campaigns:
        platform_data[campaign.platform] = platform_data.get(campaign.platform, 0) + float(campaign.budget)

    context = {
        "platform_labels": list(platform_data.keys()),
        "platform_budgets": list(platform_data.values()),
        "campaign_names": [c.name for c in campaigns],
        "clicks": [c.clicks for c in campaigns],
        "impressions": [c.impressions for c in campaigns],
    }

    return render(request, "dashboard.html", context)

@api_view(['GET'])
def usd_to_inr_rate(request):
    """
    Fetch USD to INR conversion rate using CoinGecko API
    """
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "usd",
            "vs_currencies": "inr"
        }

        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()

        data = response.json()
        return Response({
            "source": "CoinGecko",
            "usd_to_inr": data["usd"]["inr"]
        }, status=status.HTTP_200_OK)

    except requests.exceptions.RequestException as e:
        return Response(
            {"error": "Failed to fetch exchange rate"},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )
    

class CampaignViewSet(ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
