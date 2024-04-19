# Django Marketing Urls

## Description
An app to generate marketing urls for Django projects. It allows you to create marketing urls with a unique token that can be used to track the source of the traffic.


## Installation
   
    pip install django-marketing-urls

### in settings.py

    INSTALLED_APPS = [
        ...
        'marketing_urls',
        ...
    ]

### in urls.py

    urlpatterns = [
        ...
        path('marketing/', include('marketing_urls.urls')),
        ...
    ]
    
## Usage
    
### Create a marketing url

    from marketing_urls.models import MarketingUrl
    
    MarketingUrl.objects.create(original_url='https://example.com')
   

### Get the marketing url
    
        m_url = MarketingUrl.objects.get(original_url='https://example.com')
        print(m_url.marketing_url)
        
        # if you want to add extra information to the url
        from urltoken.encoder import UrlTokenEncoder
        
        token_encoder = UrlTokenEncoder('secretkey') # secretkey could be set in OS environment variable from 'URL_TOKEN_SECRET', or just leave it is None
        url_token = token_encoder.encode('my_extra_info_here')
        url_with_extra_info = m_url.marketing_url + '?t=' + url_token
        print(url_with_extra_info)


## Issues
https://github.com/laonan/django-marketing-url/issues
