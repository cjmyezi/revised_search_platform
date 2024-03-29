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
import urllib2
import json
import datetime
import ast

@require_login
def save_interaction(user, request):
    r = urllib2.unquote(request.body).decode('utf8')
    try:
        j = json.loads(r[8:])
    except ValueError:
        print("Debug Info: Request body " + request.body)
        return JsonResponse({"success": True}, status=200)
    clicked = []
    if (len(j['clicked_results'])>2):
        clicked = ast.literal_eval(j['clicked_results'])
    mouse = []
    if (len(j['mouse_moves'])>2):
        mouse = ast.literal_eval(j['mouse_moves'])
    res = InteractionTrace(
        user=user,
        start=datetime.datetime.fromtimestamp(j['start_timestamp']/1000),
        end=datetime.datetime.fromtimestamp(j['end_timestamp']/1000),
        dwell_time=j['dwell_time'],
        page_timestamps = ast.literal_eval(j['page_timestamps']),
        type=j['type'],
        origin=j['origin'],
        url=j['url'],
        serp_link=j['serp_link'],
        query=j['query'],
        mouse_moves = mouse,
        clicked_results = clicked
    )
    res.save()
    return JsonResponse({"success": True}, status=200)