#coding=utf8
import json
import sys

sys.codecs = ()
'''
from BingSE import BingSE
from BaiduCQA import BaiduCQA
#from ZhihuCQA import ZhihuCQA
'''

from Baidu import Baidu

'''
data = json.loads(BingSE('电风扇'))
fr = file('BingTemplate.html')
txt = fr.read()
fw = file('test.html', 'w')
serp = ''
for d in data:
    #print d['title'], d['snippet'], d['url'], d['html']
    serp += d['html']
fw.write(txt.replace('[SERP]', serp.encode('utf8')))
fw.close()
'''

data = json.loads(Baidu("绿叶"))
fr = file('BaiduTemplate.html')
txt = fr.read()
fw = file('test.html', 'w')
serp = ''
for d in data:
    print(d)
    serp += d
fw.write(txt.replace('[SERP]', serp.encode('utf8')))
fw.close()

'''
data = json.loads(ZhihuCQA('dota'))
for d in data:
    print d['title'], d['snippet'], d['url']
'''