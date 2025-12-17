from django.contrib import admin
from .models import Campaign
# Register your models here.

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform', 'budget', 'clicks', 'impressions', 'created_at')
    list_filter = ('platform',)
    search_fields = ('name',)
