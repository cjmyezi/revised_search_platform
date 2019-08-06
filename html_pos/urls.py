#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns

from . import views

urlpatterns = [
    url(r'task/([0-9]{1,12})/$', views.task_html_pos),
    url(r'sogou/([a-zA-Z0-9]{12})/$', views.sogou_html_pos)
]