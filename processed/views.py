import datetime

from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from CxExtractor import CxExtractor

from .models import DetailPage
from mongoengine.queryset import DoesNotExist

def get_saved_page(url):
    try:
        detailPage = DetailPage.objects.get(url=url)
    except DoesNotExist as e:
        return False, None
    else:
        return True, detailPage


def index(request):
    actual_url = request.get_full_path()[request.get_full_path().index('index/') + 6:]
    flag, detailPage = get_saved_page(actual_url)
    if flag:
        html = detailPage.html
    else:
        cx = CxExtractor(threshold=186)
        html = cx.getHtml(actual_url)

        detailPage = DetailPage()
        detailPage.html = html
        detailPage.url = actual_url
        detailPage.time = datetime.datetime.now()
        detailPage.save()

    return HttpResponse(html)