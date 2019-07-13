#coding=utf8
from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import json

rc_head = re.compile(r'(?<=<h2>).+?(?=</h2>)')
rc_url = re.compile(r'(?<=href=").+?(?=")')
rc_snippet = re.compile(r'(?<=<p>).+?(?=</p>)')
rc_src = re.compile(r'(?<=src=").+?(?=")')


def replace_url(re_compiled, origin_html, prefix):
    match = re_compiled.search(origin_html)
    replaced_html = ""
    while match:
        cur_html = origin_html[:match.end()]
        origin_html = origin_html[match.end():]
        if not match.group().startswith("http"):  
            cur_html = cur_html.replace(match.group(), prefix + match.group())
        replaced_html = replaced_html + cur_html
        match = rc_url.search(origin_html)
    return replaced_html + origin_html 


def BingSE(query):
    para = dict()
    para['query'] = query
    para['count'] = 50
    url = 'https://www.sogou.com/web?' + urllib.urlencode(para)
    req = urllib2.Request(url)
    req.add_header('Referer', 'http://www.python.org/')
    req.add_header('User-Agent','Mozilla/4.0 compatible; MSIE 5.5; Windows NT')

    with open('./request.txt', 'w') as file:
        file.write(url)
    try:
        txt = urllib2.urlopen(req).read()
    except Exception as e:
        print e
        raise e
    else:
        soup = BeautifulSoup(txt)
        serp = list()
        
        for title_html in soup.find_all('h3', class_='vrTitle'):
            next_html = list(title_html.next_siblings)
            
            sibling = '\n'.join(str(x) for x in next_html)
            title_html = str(title_html)

            html = str(title_html) + '\n' + str(sibling)
            html = "{}\n{}\n{}".format("<li class=\"b_algo\">", html, "</li>")
            with open("./html.html", 'w') as file:
                file.write(html)
            try:
                origin_url = rc_url.search(title_html).group()
                if not origin_url.startswith("http"):
                    url = 'https://www.sogou.com' + origin_url
                    html = html.replace(origin_url, url)
                else:
                    url = origin_url
            except AttributeError as e:
                print e
                url = ""

            match = rc_url.search(html)
            html = replace_url(rc_url, html, 'https://www.sogou.com')
            html = replace_url(rc_src, html, 'https://www.sogou.com')

            try:
                title  = title_html[title_html.index('>')+1:title_html.index('</a>')]
            except ValueError:
                title = ""
                
            match = rc_snippet.search(str(sibling))
            snippet = match.group() if match else ''
            
            d = {
                'url' : url,
                'title' : title,
                'snippet' : snippet,
                'html' : html
            }
            serp.append(d)
            
                    
        res = json.dumps(serp)
        return res

'''
def BingSE(query):
    para = dict()
    para['q'] = query.encode('gbk')
    para['count'] = 50
    url = 'http://www.bing.com/search?' + urllib.urlencode(para)
    try:
        txt = urllib2.urlopen(url).read()
        print(txt)
    except Exception as e:
        print e
    else:
        soup = BeautifulSoup(txt)
        serp = list()
        for result in soup.find_all('li', class_='b_algo'):
            result = str(result)
            for img in BeautifulSoup(result).find_all('img', class_='rms_img'):
                src = rc_src.search(str(img)).group()
                result = result.replace(src, 'http://www.bing.com' + src)
            d = dict()
            head = rc_head.search(result).group()
            d['url'] = rc_url.search(head).group()
            d['title'] = head[head.index('>')+1:head.index('</a>')]
            match = rc_snippet.search(result)
            if match:
                d['snippet'] = rc_snippet.search(result).group()
            else:
                d['snippet'] = ''
            d['html'] = result
            serp.append(d)
        res = json.dumps(serp)
        return res
'''


if __name__ == '__main__':
    data = json.loads(BingSE('凤凰'))
    for d in data:
        print d['title'], d['snippet'], d['url']
