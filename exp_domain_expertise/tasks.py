#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'defaultstr'


task_url = 'exp_domain_expertise'

task_steps = [
    'description',
    'pre_task_question',
    'search',
    'post_task_question',
    'query_satisfaction',
]


class Task(object):
    def __init__(self,
                 task_id=None,
                 name=None,
                 description=None,
                 **kwargs):
        self.task_id = task_id
        self.name = name
        self.description = description
        for key in kwargs:
            self.__dict__[key] = kwargs[key]

tasks = [
    Task(
        task_id='0',
        name=u'样例任务',
        description=u'样例任务',
    ),
    Task(
        task_id='1',
        name=u'任务1',
        description=u'问：请问我国颗粒物污染特征有哪些？请从全国、地区层面，时间变化层面、颗粒物组成层面等角度进行分析。',
    ),
    Task(
        task_id='2',
        name=u'任务2',
        description=u'问：简述郁金香狂热事件（Tulip Mania）（200字以内）',
    ),
    Task(
        task_id='3',
        name=u'任务3',
        description=u'问：简述汇率对经济的影响。',
    ),
    Task(
        task_id='4',
        name=u'任务4',
        description=u'问：纯牛奶的功效与作用。',
    ),
    Task(
        task_id='5',
        name=u'任务5',
        description=u'问：骨质增生是什么原因引起的？',
    ),
    Task(
        task_id='6',
        name=u'任务6',
        description=u'问：内分泌失调能引起血压升高吗？',
    ),
    Task(
        task_id='7',
        name=u'任务7',
        description=u'问：什么是责任分散（旁观者）效应，及如何避免责任分散效应？',
    ),
    Task(
        task_id='8',
        name=u'任务8',
        description=u'问：边缘性人格障碍的诊断标准是什么？',
    ),
    Task(
        task_id='9',
        name=u'任务9',
        description=u'问：地震的等级和烈度有什么区别？',
    ),
    Task(
        task_id='10',
        name=u'任务10',
        description=u'问： 加州为什么山火频发？',
    ),
]
