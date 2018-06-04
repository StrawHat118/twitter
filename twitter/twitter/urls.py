"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from weibo import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^post/$',views.posting),
    url(r'^testChangeTime/$',views.changeTime),
    url(r'^addContractTest/$',views.add_contract_test_v),
    url(r'^addContractYw/$',views.add_contract_yw_v),
    url(r'^releaseProgramTest/$',views.releaseProgrsmTestV),
    url(r'^releaseProgramYw/$',views.releaseProgramYwV),
    url(r'^interfaceTest/$' ,views.interfaceTest),
]
