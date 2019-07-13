#coding=utf8
from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import json

rc_url = re.compile(r'(?<=href=").+?(?=")')
blacklist_domain = ["zhidao.baidu.com", "zhihu.com"]

def Baidu(query):
    fw = file('Baidu.txt', 'w')
    para = dict()
    fw.write(query + '\n')
    para['wd'] = query
    para['rn'] = 50
    url = 'http://www.baidu.com/s?' + urllib.urlencode(para)
    fw.write(url + '\n')
    try:
        txt = urllib2.urlopen(url).read()
    except Exception as e:
        print e
    else:
        soup = BeautifulSoup(txt)
        serp = list()
        for result in soup.find_all('div', class_='result c-container'):
            result = str(result)
            s = BeautifulSoup(result)
            d = dict()
            head = str(s.h3)
            d['url'] = rc_url.search(head).group()
            d['title'] = s.h3.text
            d['snippet'] = str(s.find('div', 'c-abstract'))
            result = result.replace(d['url'], 'http://127.0.0.1:8000/processed/index/' + d['url'])
            d['html'] = result
            serp.append(d)
        res = json.dumps(serp)

        return res

if __name__ == '__main__':
    data = json.loads(Baidu('电风扇'))

    for d in data:
        print d
