from django.conf.urls import url
from .views import \
    (CustomerProfileListView,
     CustomerProfileCreateView,
     CustomerProfileUpdateView,
     GroupCreateView,
     GroupUpdateView,
     GroupListView,
     GroupZoneDetailView,
     GroupDetailView
     )

urlpatterns = [
    url(r'^customers/$', CustomerProfileListView.as_view(), name='customer-list'),
    url(r'^customers/create/$', CustomerProfileCreateView.as_view(), name='customer-create'),
    url(r'^customers/(?P<pk>[0-9]+)/$', CustomerProfileUpdateView.as_view(), name='customer-detail'),

    url(r'^$', GroupListView.as_view(), name='group-list'),
    url(r'^create/$', GroupCreateView.as_view(), name='group-create'),
    url(r'^(?P<pk>[0-9]+)/update$', GroupUpdateView.as_view(), name='group-update'),
    url(r'^(?P<pk>[0-9]+)/detail$', GroupDetailView.as_view(), name='group-detail'),
    url(r'^(?P<pk>[0-9]+)/zone/(?P<zone_id>[0-9]+)/$', GroupZoneDetailView.as_view(), name='group-zone-detail'),

    # pdf url
    # url(r'^pdf/$', CustomerListPDF.as_view(), name='customer-list-pdf')
]
