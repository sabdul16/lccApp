# in image_app/urls.py
from django.urls import path
from .views import image_compare_api, home


urlpatterns = [
    path('', home, name='home'),
    path('compare/', image_compare_api, name='api-compare'),
]
