#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'cjm'
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import JsonResponse
from user_system.utils import require_login
import task_manager.utils as task_utils
from .models import *
import logging

logger = logging.getLogger(__name__)

@require_login
def save_interaction(user, request):
    print(user.username)
    print(request.method)
    print(request.body)
    return JsonResponse({"success":True}, status=200)