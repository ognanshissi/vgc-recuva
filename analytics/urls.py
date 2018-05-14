from django.conf.urls import url
from .views import AnalyticsHomeView

app_name='analytics'

urlpatterns = [
    url(r'^$', AnalyticsHomeView.as_view(), name='home')
]