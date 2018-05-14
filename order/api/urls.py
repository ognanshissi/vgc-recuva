from django.conf.urls import url, include
from .views import OrderCreateListAPIView


urlpatterns = [
    url(r'^$', OrderCreateListAPIView.as_view(), name='crud'),
]