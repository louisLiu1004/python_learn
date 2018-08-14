
# 百度图片爬虫，单线程

import requests
import os
import re
import urllib.parse as up
import _md5
import tqdm
import time
import math

def get_imageURL(word,index):
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    try:
        response = requests.get('https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={0}&pn={1}'.format(up.quote(word),index),headers=headers).text
        patternt = re.compile('flip.setData.*?imgData\'.*?{}]}\)')
        results = re.search(patternt,response).group()
        patternt2 = re.compile('"objURL":"(.*?)"')
        objURL = re.findall(patternt2,results)
        if len(objURL)>0:
            for URL in tqdm.tqdm(objURL,desc='\033[0;34;m正在下载...\033[0m《\033[0;32;m{}\033[0m》\033[0;34;m第{}-{}页\033[0m'.format(word,int((index/20)+1),int((index/20)+3))):
                iname = parse_iamgeName(URL)
                save_image(URL,iname,word)
        else:
             print('《\033[0;32;m{}\033[0m》没有\033[0;34;m第{}-{}页\033[0m'.format(word,int((index/20)+1),int((index/20)+3)))
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
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    try:
        response = requests.get(url,headers=headers,timeout = 10)
        if response.status_code == 200:
            content = response.content #.content为了获取到图片的bytes格式文件
            # 在当前目录创建文件夹
            path = r'{0}\baodu_images\{1}'.format(os.getcwd(),word)
            if not os.path.exists(path):
                os.makedirs(path)
            # 创建md5文件名，方便检测文件的唯一性
            file_path = path+'\{0}{1}'.format(_md5.md5(content).hexdigest(),iname)
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(content)
                    f.close()
        else:
            return None
    except requests.RequestException as E:
        path = r'{0}\baodu_images\{1}\Timeout.txt'.format(os.getcwd(), word)
        with open(path,'a') as f:
            f.write('超时页面:'+url+'\n')
            f.close()
        # print('\n\033[0;31;m请求下载页面超时跳过:{}\033[0m'.format(url))


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
    for i in range(int(math.ceil(page/3))):
        main(word,i*60)

    time.sleep(0.5)
    print('爬虫运行结束:...{}'.format(time.ctime()))
    end = time.time()
    print('爬虫一共运行...{}秒'.format(end-start))
