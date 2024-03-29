#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'defaultstr'

from .bing_api import BingSE
from .baidu_api import Baidu
from .zhihu_api import ZhihuCQA
from .sogou_api import Sogou
from .models import *
import json


def _crawl(query, search_engine, result_class, results_class):
    results = json.loads(search_engine(query.encode('utf8')))
    res_docs = []
    for r in results:
        r_doc = result_class(
            title=r['title'],
            url=r['url'],
            snippet=r['snippet'],
            html_content=r['html'],
        )
        res_docs.append(r_doc)
    results_doc = results_class(query=query, results=res_docs)
    results_doc.save()
    try:
        return results_class.objects.get(query=query)
    except DoesNotExist:
        return None


def crawl_bing(query):
    return _crawl(query, BingSE.BingSE, BingResult, BingResults)


def crawl_baidu_cqa(query):
    return _crawl(query, BaiduCQA.BaiduCQA, BaiduCQAResult, BaiduCQAResults)

def crawl_baidu(query):
    return _crawl(query, Baidu.Baidu, BaiduResult, BaiduResults)

def crawl_zhihu(query):
    return _crawl(query, ZhihuCQA.ZhihuCQA, ZhihuResult, ZhihuResults)

def crawl_sogou(query):
    return _crawl(query, Sogou.Sogou, SogouResult, SogouResults)


