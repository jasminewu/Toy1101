
# -*- coding:UTF-8 -*-

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
    #函数是一级对象，可以像对象一样直接传递
    #r表示^time/$这是一个原始字符串
    #^头部匹配 $尾部匹配#URL
    模式以及要为该 URL 模式调用的视图函数之间的映射表
    #将URL映射到视图
"""
from django.conf.urls import url
from mysite import views
urlpatterns = [
    url(r'^time/$',views.current_datetime),

]
