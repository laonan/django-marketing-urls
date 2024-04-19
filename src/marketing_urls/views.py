from django.shortcuts import redirect
from django.utils import timezone
from django.http import Http404
from urltoken.encoder import UrlTokenEncoder
from .utils import get_client_ip
from .models import MarketingUrl, VisitorLog


def marketing_link(request, marketing_url_key):
    try:
        marketing_url = MarketingUrl.objects.get(marketing_url_key=marketing_url_key)
        if marketing_url.end_time is not None:
            if marketing_url.end_time < timezone.now():
                return Http404

        token = request.GET.get('t', None)
        if token is not None:
            token_encoder = UrlTokenEncoder()
            try:
                decoded_token = token_encoder.decode(token)
            except Exception as e:
                decoded_token = f'{e} {token}'
            VisitorLog.objects.create(url=marketing_url, url_decoded_token=decoded_token, ip=get_client_ip(request))
        else:
            VisitorLog.objects.create(url=marketing_url, ip=get_client_ip(request))

        return redirect(marketing_url.original_url)
    except MarketingUrl.DoesNotExist:
        return Http404
