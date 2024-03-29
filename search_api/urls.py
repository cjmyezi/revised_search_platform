#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'defaultstr'

from django.conf.urls import url, patterns

from . import views

urlpatterns = [
    url(r'^bing/$', views.bing_search),
    url(r'^baidu_cqa/$', views.baidu_cqa_search),
    url(r'^baidu/$', views.baidu_search),
    url(r'^zhihu/$', views.zhihu_search),
    url(r'^sogou/$', views.sogou_search),
]

