#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'cjm'

from django.conf.urls import url, patterns

from . import views

urlpatterns = [
    url(r'^save_interaction/$', views.save_interaction)
]
