
# 百度图片爬虫，单线程

import requests
import os
import re
from urllib.parse import quote
from _md5 import md5
from requests import RequestException
from tqdm import tqdm
import time

def get_imageURL(word,index):
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    try:
        response = requests.get('https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={0}pn={1}'.format(quote(word),index)).text
        patternt = re.compile('flip.setData.*?imgData\'.*?{}]}\)')
        results = re.search(patternt,response).group()
        patternt2 = re.compile('"objURL":"(.*?)"')
        objURL = re.findall(patternt2,results)
        for URL in tqdm(objURL,desc='\033[0;34;m正在下载...\033[0m《\033[0;32;m{}\033[0m》\033[0;34;m第{}页\033[0m'.format(word,int((index/20)+1))):
            iname = parse_iamgeName(URL)
            save_image(URL,iname,word)
    except Exception as E:
        print(E)
        # print('请求网页异常')
def parse_iamgeName(URL):
    image_name = '.jpg'
    if '.jpg' in URL:
        image_name = '.jpg'
    elif '.png' in URL:
        image_name = '.png'
    elif '.gif' in URL:
        image_name = '.gif'
    elif '.bmp' in URL:
        image_name = '.bmp'
    return image_name
def save_image(url,iname,word):
    try:
        response = requests.get(url,timeout = 30)
        if response.status_code == 200:
            content = response.content #.content为了获取到图片的bytes格式文件
            # 在当前目录创建文件夹
            path = r'{0}\baodu_images\{1}'.format(os.getcwd(),word)
            if not os.path.exists(path):
                os.makedirs(path)
            # 创建md5文件名，方便检测文件的唯一性
            file_path = path+'\{0}{1}'.format(md5(content).hexdigest(),iname)
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(content)
                    f.close()
        else:
            return None
    except RequestException as E:
        print('\n\033[0;31;m请求下载页面超时跳过:{}\033[0m'.format(url))


def main(word,index):
    get_imageURL(word,index)

if __name__=='__main__':
    print(''' _____       ___   _   _____   _   _   _       ___  ___       ___   _____   _____
|  _  \     /   | | | |  _  \ | | | | | |     /   |/   |     /   | /  ___| | ____|
| |_| |    / /| | | | | | | | | | | | | |    / /|   /| |    / /| | | |     | |__
|  _  {   / / | | | | | | | | | | | | | |   / / |__/ | |   / / | | | |  _  |  __|
| |_| |  / /  | | | | | |_| | | |_| | | |  / /       | |  / /  | | | |_| | | |___
|_____/ /_/   |_| |_| |_____/ \_____/ |_| /_/        |_| /_/   |_| \_____/ |_____| ''')
    word = input('\033[0;34;m请输入关键字:..\033[0m')
    page = int(input('\033[0;34;m请输入想要爬取的页数:..\033[0m'))
    print('爬虫运行开始:...{}'.format(time.ctime()))
    start = time.time()
    for i in range(page):
        main(word,i*20)
    print('爬虫运行结束:...{}'.format(time.ctime()))
    end = time.time()
    print('爬虫一共运行...{}秒'.format(end-start))
