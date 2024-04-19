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

    
## Usage
    
    from urltoken.encoder import UrlTokenEncoder
    
    encoder =  UrlTokenEncoder('yoursecretkey')
    token = encoder.encode('example@domain.com')
    print(token)

    decoded = encoder.decode(token)
    print(decoded)


## Issues
https://github.com/laonan/urltoken/issues
