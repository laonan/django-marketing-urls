import os
from django.db import models
from django.urls import reverse
from .utils import new_key


class MarketingUrl(models.Model):
    marketing_url_key = models.CharField(max_length=40, default=new_key, editable=False, unique=True)
    original_url = models.URLField()
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.marketing_url_key} ({self.original_url})'

    @property
    def marketing_url(self):
        url = reverse('marketing_link', kwargs={'marketing_url_key': self.marketing_url_key})
        if os.getenv('BASE_URL'):
            return f'{os.getenv("BASE_URL")}{url}'
        return url


class VisitorLog(models.Model):
    url = models.ForeignKey(MarketingUrl, on_delete=models.CASCADE)
    url_decoded_token = models.TextField(null=True, blank=True)
    ip = models.GenericIPAddressField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.url)
