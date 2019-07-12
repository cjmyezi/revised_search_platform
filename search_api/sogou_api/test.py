#coding=utf8
import json
'''
from BingSE import BingSE
from BaiduCQA import BaiduCQA
#from ZhihuCQA import ZhihuCQA
'''

from Sogou import Sogou

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

data = json.loads(Sogou("绿叶"))
fr = file('Sogou.html')
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