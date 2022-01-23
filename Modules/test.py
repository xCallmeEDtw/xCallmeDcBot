from lxml.html import fromstring
import requests
from itertools import cycle
import traceback

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

uw = {
'http': 'http://10.10.1.10:3128',
'https': 'http://10.10.1.10:1080',
}

#If you are copy pasting proxy ips, put in the list below
#proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']
proxies = get_proxies()
proxy_pool = cycle(proxies)

url = 'https://www.google.com/'
proxy = next(proxy_pool)
#response = requests.get(url,proxies={"http": proxy, "https": proxy})
a = "http://" +  proxy
r = requests.get(url,proxies={"http":'210.6.97.41', "https": '210.6.97.41'})

  