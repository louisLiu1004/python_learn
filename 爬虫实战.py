# 猫眼Top100案例
# import requests
# from requests import RequestException
# from multiprocessing import Pool
# import re
# import json
#
# def get_page(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             print('ok online')
#             return response.text
#         else:
#             pass
#     except RequestException as e:
#         print(e)
# def parse_page(get_html):
#     pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
#                          +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
#                          +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
#     results = re.findall(pattern,get_html)
#     for item in results:
#         yield {
#             '排名':item[0],
#             '片名': item[2],
#             '演员': item[3].strip()[3:],
#             '上映时间': item[4].strip()[5:],
#             '分数': item[5]+item[6]
#         }
# def write_to_file(content):
#     with open('Top100.txt','a',encoding='utf-8') as f:
#         f.write(json.dumps(content,ensure_ascii=False)+'\n')
#         f.close()
# def main(offset):
#     url ='http://maoyan.com/board/4?offset='+str(offset)
#     get_html = get_page(url)
#
#     for item in parse_page(get_html):
#         print(item)
#         write_to_file(item)
#
# if __name__ == '__main__':
#     for i in range(10):
#         main(i*10)
#     pool = Pool()
#     pool.map(main, [i*10 for i in range(10)])




# 今日头条图片实战
import os
from _md5 import md5
from urllib.parse import urlencode
import json
import requests
import re
from bs4 import BeautifulSoup
from requests import RequestException
from tqdm import tqdm
import time
from multiprocessing import Pool

def get_page_index(offset,keyword):
    data ={
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3,
    }
    url = 'https://www.toutiao.com/search_content/?'+ urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException :
        print('\033[0;31;m请求网页错误:{}\033[0m'.format(url))
def parse_page_index(get_html):
    data = json.loads(get_html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')
def get_page_detail(detail_url):
    headers = {
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 53.0.2785.104Safari / 537.36Core / 1.53.4882.400QQBrowser / 9.7.13059.400'
    }
    try:
        response = requests.get(detail_url,headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException :
        print('\033[0;31;m请求详情页面错误:{}\033[0m'.format(detail_url))
def parse_page_detail(get_html_detail,detail_url):
    soup = BeautifulSoup(get_html_detail,'lxml')
    title = soup.select('title')[0].text
    images_pattern = re.compile('JSON.parse\("(.*?)"]}', re.S)
    try:
        results = re.findall('"http://.*?"',re.sub('\\\\','',re.search(images_pattern,get_html_detail).group(1)))
        results_strip =[results[i].strip('"')  for i in range(len(results))]
        url_list = []
        for url in results_strip:
            if url not in url_list:
                url_list.append(url)
        # 调取下载图片函数
        for url in tqdm(url_list,desc='\033[0;34;m正在下载图集...\033[0m《\033[0;32;m{}\033[0m》'.format(title)):
            save_image(url)
        return {
            'title':title,
            'url':detail_url,
            'images':url_list
        }
    except Exception:
        print('\033[0;31;m忽略错误链接：{}\033[0m'.format(detail_url))

def save_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content
            # 在当前目录创建文件夹
            path = r'{}\toutiao-images'.format(os.getcwd())
            if not os.path.exists(path):
                os.makedirs(path)
            # 创建md5文件名，方便检测文件的唯一性
            file_path = path+'\{0}.png'.format(md5(content).hexdigest())
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(content)
                    f.close()
        else:
            return None
    except RequestException:
        print('\033[0;31;m请求下载页面错误:{}\033[0m'.format(url))

def main(index):
    get_html = get_page_index(index,'街拍')
    for detail_url in parse_page_index(get_html):
       get_html_detail = get_page_detail(detail_url)
       if get_html_detail:
           result = parse_page_detail(get_html_detail,detail_url)


if __name__ == '__main__':
    print('爬虫运行开始:...{}'.format(time.ctime()))
    start = time.time()
    pool = Pool(5)
    pool.map(main,[i*20 for i in range(10)])
    print('爬虫运行结束:...{}'.format(time.ctime()))
    end = time.time()
    print('爬虫一共运行...{}秒'.format(end-start))