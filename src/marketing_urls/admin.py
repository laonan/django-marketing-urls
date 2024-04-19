from django.contrib import admin
from .models import MarketingUrl, VisitorLog


@admin.register(MarketingUrl)
class MarketingUrlAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'marketing_url_key', 'end_time')
    search_fields = ('original_url', 'marketing_url_key')


@admin.register(VisitorLog)
class VisitorLogAdmin(admin.ModelAdmin):
    list_display = ('url', 'ip', 'url_decoded_token', 'create_time')
    search_fields = ('url', 'ip', 'url_decoded_token')

