"""project2 URL Configuration

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
# from django.contrib import admin
from app2.views import snippet_list, snippet_detail, SnippetList, SnippetDetail,UserDetail,UserList

#add data format : http://example.com/api/items/4/.json
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import include

urlpatterns = [
    # url(r'^snippets/$', snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail),
    url(r'^snippets/$', SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view()),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
