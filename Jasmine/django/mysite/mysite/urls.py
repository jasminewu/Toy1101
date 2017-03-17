"""mysite URL Configuration

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
from lean import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', views.index),
    url(r'^add/$', views.add, name='add'),
    #/add3/?a=4&b=5
    url(r'^add3/$',views.add),
    #/newadd/4/5/
    url(r'^newadd/(\d+)/(\d+)/$', views.add2, name='add2'),
    url(r'^add/(\d+)/(\d+)/$', views.old_add2_redirect),

    url(r'^$', views.index2),
    url(r'^home/$', views.home, name='home'),
    url(r'^form/$', views.form, name='form'),
    url(r'^form2/$', views.form2, name='form2'),




]
