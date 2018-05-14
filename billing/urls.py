from django.conf.urls import url
from .views import UpdateBillingView, BillingListView


urlpatterns = [
    url(r'^$', BillingListView.as_view(), name='billing-list'),
]

