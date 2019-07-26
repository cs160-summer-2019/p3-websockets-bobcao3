# chat/urls.py
from django.conf.urls import url

from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('mobile/',views.mobile, name='mobile'),
    path('large/',views.large, name='large'),
    path('scanqr/',views.scanqr, name='scanqr'),
]

