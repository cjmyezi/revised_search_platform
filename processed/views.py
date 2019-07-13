from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from CxExtractor import CxExtractor


def index(request):
    actual_url = request.get_full_path()[request.get_full_path().index('index/') + 6:]
    print actual_url
    cx = CxExtractor(threshold=186)
    html = cx.getHtml(actual_url)
    return HttpResponse(html)