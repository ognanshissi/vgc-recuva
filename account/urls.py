from django.conf.urls import url, include
from .views import AccountLoginView, AccountLogoutView
from django.contrib.auth.views import LogoutView

app_name = 'account'

urlpatterns = [
    url(r'^login/$', AccountLoginView.as_view(), name='login'),
    url(r'^logout/$', AccountLogoutView.as_view(), name='logout')
]