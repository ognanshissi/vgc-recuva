from django.conf.urls import url
from .views import (
    OrderListView,
    OrderDetailView,
    DeliveredOrderView,
    OrderCreateView,
    CompletePaymentView,
    CancelDeliveredOrderView
)
from billing.views import UpdateBillingView

urlpatterns = [
    url(r'^$', OrderListView.as_view(), name='order-list'),
    url(r'^create/$', OrderCreateView.as_view(), name='order-create'),

    url(r'^(?P<order_id>[0-9a-zA-Z]+)/delivered/$',
        DeliveredOrderView.as_view(),
        name='order-delivered'),

    url(r'^(?P<order_id>[0-9a-zA-Z]+)/cancel/$',
        CancelDeliveredOrderView.as_view(),
        name='order-cancel'),

    url(r'^(?P<order_id>[0-9a-zA-Z]+)/complete/$',
        CompletePaymentView.as_view(),
        name='order-complete'),

    url(r'^(?P<order_id>[0-9a-zA-Z]+)/$',
        OrderDetailView.as_view(),
        name='order-detail'),

    url(r'^(?P<order_id>[0-9a-zA-Z]+)/update/(?P<pk>[0-9]+)/billing$',
        UpdateBillingView.as_view(),
        name='order-billing-update')
]
