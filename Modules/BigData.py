# import os
# import requests
# from bs4 import BeautifulSoup as mBS
# import random
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from time import sleep

# from lxml.html import fromstring
# def get_proxies():
#     url = 'https://free-proxy-list.net/'
#     response = requests.get(url)
#     parser = fromstring(response.text)
#     proxies = set()
#     for i in parser.xpath('//tbody/tr')[:10]:
#         if i.xpath('.//td[7][contains(text(),"yes")]'):
#             #Grabbing IP and corresponding PORT
#             proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
#             proxies.add(proxy)
#     return proxies
 





# def RandomPicture(text):
#     # if text == '':
#     web = 'https://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers&page=500'
#     # else:
#     #     web = f'https://wall.alphacoders.com/search.php?search={text}'
#     headers= {
#     # ':authority' : 'wall.alphacoders.com',
#     # ':method' :'GET',
#     # ':path' :'/by_category.php?id=3&name=Anime+Wallpapers',
#     # ':scheme' : 'https',
#     # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     # 'accept-encoding': 'gzip, deflate, br',
#     # 'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#     # 'cache-control': 'max-age=0',
#     # 'referer': 'https://www.google.com/',
#     # 'sec-fetch-dest': 'document',
#     # 'sec-fetch-mode': 'navigate',
#     # 'sec-fetch-site': 'cross-site',
#     # 'sec-fetch-user': '?1',
#     # 'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
#     }
#     proxy_list = [
#     '183.95.80.102:8080',
#     '123.160.31.71:8080',
#     '115.231.128.79:8080',
#     '166.111.77.32:80',
#     '43.240.138.31:8080',
#     '218.201.98.196:3128'
#     ]


#     proxy = random.choice(proxy_list)
#     proxies = {
#     'http': 'http://10.10.1.10:3128',
#     'https': 'http://10.10.1.10:1080',
#     }

#     r = requests.get(web,headers=headers)
#     print(r.status_code)
#     myreply = []
#     soup = mBS(r.text, 'html.parser')
#     cards = (soup.select('[loading="lazy"]'))
#     for i in range(0,len(cards),2):
#         myreply.append(cards[i]['src'])
#     MyRan =  random.randint(0,len(myreply)-1)
#     #print(myreply,MyRan)
#     return myreply[MyRan]



# # def RandomPicture(text):
# #     print('123')
# #     myreply = []
# #     options = Options()
# #     options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# #     options.add_argument("--disable-notifications")
# #     options.add_argument("--headless") #無頭模式
# #     options.add_argument("--disable-dev-shm-usage")
# #     options.add_argument("--no-sandbox")
# #     print('345')
# #     #chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
# #     chrome = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
# #     chrome.get('https://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers&page=500')
# #     sleep(10)
# #     soup = mBS(chrome.page_source, 'html.parser')
# #     print(soup)
# #     cards = (soup.select('[loading="lazy"]'))
    
# #     print(cards)
# #     for i in range(0,len(cards),2):
# #        # print(cards[i])
# #         myreply.append(cards[i]['src'])
# #     MyRan =  random.randint(0,len(myreply))
# #     #print(myreply,MyRan)
# #     return myreply[MyRan]