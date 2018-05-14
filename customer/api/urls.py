from django.conf.urls import url, include
from .views import GroupZoneCreateAPIView


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/zone/$', GroupZoneCreateAPIView.as_view(), name='zone-create'),
]