from django.urls import path
from .views import marketing_link

urlpatterns = [
    path('t/<str:marketing_url_key>/', marketing_link, name='marketing_link'),
]
