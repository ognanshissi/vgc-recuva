from django.conf.urls import url, include
from .views import AnalyticsView, AnalyticsBillingView


urlpatterns = [
    url(r'^$', AnalyticsView.as_view(), name='list'),
    url(r'^test/$', AnalyticsBillingView.as_view())
]