from django.conf.urls import url
from .views import TestApi



urlpatterns = [
    url(r'^testapi$', TestApi.as_view(), name='home'),
   
]