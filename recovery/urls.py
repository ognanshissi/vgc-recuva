"""recovery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import HomepageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomepageView.as_view(), name='home'),

    # account URLS
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^products/', include('products.urls', namespace='product')),
    url(r'^billings/', include('billing.urls', namespace='billing')),
    url(r'^orders/', include('order.urls', namespace='order')),
    url(r'^api/orders/', include('order.api.urls', namespace='api-order')),
    url(r'^groups/', include('customer.urls', namespace='customer')),
    url(r'^api/groups/', include('customer.api.urls', namespace='api-customer')),
    url(r'^analytics/', include('analytics.urls', namespace='analytics')),
    url(r'^api/analytics/', include('analytics.api.urls', namespace='api-analytics')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
