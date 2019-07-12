#coding=utf8
from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import json

rc_url = re.compile(r'(?<=href=").+?(?=")')

def Sogou(query):
    fw = file('Sogou.txt', 'w')
    para = dict()
    fw.write(query + '\n')
    para['query'] = query
    url = 'https://www.sogou.com/web?' + urllib.urlencode(para)
    fw.write(url + '\n')

    try:
        txt = urllib2.urlopen(url).read()
        fw.write(txt)
        fw.close()
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
            d['snippet'] = s.find('div', 'c-abstract')
            d['html'] = result
            serp.append(d)
        res = json.dumps(serp)


        return res

if __name__ == '__main__':
    data = json.loads(Sogou('电风扇'))

    for d in data:
        print d
