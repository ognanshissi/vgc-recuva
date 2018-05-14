from django.conf.urls import url
from .views import (
    TypeListView,
    TypeCreateView,
    TypeUpdateView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView
)

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='product-list'),
    url(r'^create/$', ProductCreateView.as_view(), name='product-create'),
    url(r'^(?P<pk>[0-9]+)/update/$', ProductUpdateView.as_view(), name='product-update'),
    url(r'^types/$', TypeListView.as_view(), name='type-list'),
    url(r'types/create/$', TypeCreateView.as_view(), name='type-create'),
    url(r'types/(?P<pk>[0-9]+)/update/$', TypeUpdateView.as_view(), name='type-update')
]
