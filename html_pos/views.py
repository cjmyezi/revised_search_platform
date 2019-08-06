from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
import urllib
from .models import *
import exp_domain_expertise.tasks as tks
import exp_domain_expertise.utils as tuils
import utils


try:
    import simplejson as json
except ImportError:
    import json


def task_html_pos(request, task_id):
    task = tuils.get_task_by_id(task_id)
    init_html = task.init_html
    return render_to_response(
        'server_page.html',
        {
            'task_id': task_id,
            'html': init_html,
        },
        RequestContext(request),
    )


def sogou_html_pos(request, last_time):
    page = utils.get_sogoupage_obj(_last_time=int(last_time))
    if page is None:
        return HttpResponse('No sogou page to get')
    html = page.html
    start_time = page.start_timestamp
    return render_to_response(
        'sogou_page.html',
        {
            'start_time': start_time,
            'html': html,
        },
        RequestContext(request),
    )


@csrf_exempt
def receive_pos(request, task_id):
    print('receive pos', request)
    if request.method == 'POST':
        # print(request.POST.get('pos'))
        pos_list = json.loads(request.POST.get('pos'))
        tmp_list = []
        for item in pos_list:
            item_pos = ItemPos()
            id_, type_ = item['eid'].strip().split('_')
            item_pos.result_type = type_
            item_pos.item_id = int(id_)
            item_pos.left = item['absLeft']
            item_pos.top = item['absTop']
            item_pos.width = item['offsetWidth']
            item_pos.height = item['offsetHeight']
            tmp_list.append(item_pos)
        print('get all pos of task_id, #pos=%d, task_id=%s' % (len(tmp_list), task_id))
        positions = Positions()
        positions.task_id = task_id
        positions.item_pos = tmp_list
        positions.save()
    return HttpResponse('success')


@csrf_exempt
def receive_pos_sogou(request, start_time):
    print('receive pos', request)
    if request.method == 'POST':
        # print(request.POST.get('pos'))
        page = PageLog.objects.get(start_timestamp=int(start_time))
        pos_list = json.loads(request.POST.get('pos'))
        tmp_list = []
        for item in pos_list:
            item_pos = ItemPos()
            id_, type_ = item['eid'].strip().split('_')
            item_pos.result_type = type_
            item_pos.item_id = int(id_)
            item_pos.left = item['absLeft']
            item_pos.top = item['absTop']
            item_pos.width = item['offsetWidth']
            item_pos.height = item['offsetHeight']
            tmp_list.append(item_pos)
        print('get all pos, #pos=%d, start_time=%s' % (len(tmp_list), start_time))
        positions = SogouPositions()
        positions.page = page
        positions.item_pos = tmp_list
        positions.save()
    return HttpResponse('success')


def send_success(request, task_id):
    print('in send success', request)
    if int(task_id) < 20:
        next_id = '%d' % (int(task_id) + 1)
        url = '/heatmaps/server_pos/' + next_id + '/'
        return HttpResponseRedirect(url)
    else:
        return HttpResponse('Get server page position success')