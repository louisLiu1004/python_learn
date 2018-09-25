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
# import os
# from _md5 import md5
# from urllib.parse import urlencode
# import json
# import requests
# import re
# from bs4 import BeautifulSoup
# from requests import RequestException
# from tqdm import tqdm
# import time
# from multiprocessing import Pool
#
# # 请求首页信息
# def get_page_index(index,keyword):
#     data ={
#         'offset': index,
#         'format': 'json',
#         'keyword': keyword,
#         'autoload': 'true',
#         'count': 20,
#         'cur_tab': 3,
#         'from': 'gallery'
#     }
#     url = 'https://www.toutiao.com/search_content/?'+ urlencode(data)
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.text
#         else:
#             return None
#     except RequestException :
#         print('\033[0;31;m请求网页错误:{}\033[0m'.format(url))
#
# # 解析出首页每个标题对应的链接
# def parse_page_index(get_html):
#     data = json.loads(get_html)
#     if data and 'data' in data.keys():
#         for item in data.get('data'):
#             yield item.get('article_url') #提取article_url制作生成器，可以迭代
#
# # 请求标题链接的内容
# def get_page_detail(detail_url):
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
#     }
#     try:
#         response = requests.get(detail_url,headers=headers)
#         if response.status_code == 200:
#             return response.text
#         else:
#             return None
#     except RequestException :
#         print('\033[0;31;m请求详情页面错误:{}\033[0m'.format(detail_url))
#
# # 从标题链接内容中解析每张图片的超链接
# def parse_page_detail(get_html_detail,detail_url):
#     soup = BeautifulSoup(get_html_detail,'lxml')
#     # 设立正则匹配规则
#     images_pattern = re.compile('JSON.parse\("(.*?)"]}', re.S)
#     try:
#         # 获取当前链接的标题
#         title = soup.select('title')[0].text
#         results = re.findall('"http://.*?"',re.sub('\\\\','',re.search(images_pattern,get_html_detail).group(1)))
#         results_strip =[results[i].strip('"')  for i in range(len(results))] #获取到当前标题下所有图片超链接
#         url_list = []
#         # 排除掉同名链接
#         for url in results_strip:
#             if url not in url_list:
#                 url_list.append(url)
#         # 调取下载图片函数
#         for url in tqdm(url_list,desc='\033[0;34;m正在下载图集...\033[0m《\033[0;32;m{}\033[0m》'.format(title)): #用tqdm模块做进度条
#             save_image(url,title)
#         return {
#             'title':title,
#             'url':detail_url,
#             'images':url_list
#         }
#     except Exception:
#         print('\033[0;31;m忽略错误链接：{}\033[0m'.format(detail_url))
#
# # 保存图片
# def save_image(url,title):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             content = response.content #.content为了获取到图片的bytes格式文件
#             # 在当前目录创建文件夹
#             path = r'{0}\toutiao-images\{1}'.format(os.getcwd(),title)
#             if not os.path.exists(path):
#                 os.makedirs(path)
#             # 创建md5文件名，方便检测文件的唯一性
#             file_path = path+'\{0}.png'.format(md5(content).hexdigest())
#             if not os.path.exists(file_path):
#                 with open(file_path,'wb') as f:
#                     f.write(content)
#                     f.close()
#         else:
#             return None
#     except RequestException:
#         print('\033[0;31;m请求下载页面错误:{}\033[0m'.format(url))
#
# # 主函数入口
# def main(index):
#     get_html = get_page_index(index,'裸漏') #传递offset量和搜索关键字 给主页做链接
#     for detail_url in parse_page_index(get_html):
#        get_html_detail = get_page_detail(detail_url)
#        if get_html_detail:
#            result = parse_page_detail(get_html_detail,detail_url)
#
#
# if __name__ == '__main__':
#     print('爬虫运行开始:...{}'.format(time.ctime()))
#     start = time.time()
#     pool = Pool(5)
#     pool.map(main,[i*20 for i in range(10)])
#     print('爬虫运行结束:...{}'.format(time.ctime()))
#     end = time.time()
#     print('爬虫一共运行...{}秒'.format(end-start))

# 实战爬取百度图片
# import requests
# import os
# import re
# from urllib.parse import quote
# from _md5 import md5
# from requests import RequestException
# from tqdm import tqdm
# import time
#
# def get_imageURL(word,index):
#     headers = {
#             'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
#         }
#     try:
#         response = requests.get('https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={0}pn={1}'.format(quote(word),index)).text
#         patternt = re.compile('flip.setData.*?imgData\'.*?{}]}\)')
#         results = re.search(patternt,response).group()
#         patternt2 = re.compile('"objURL":"(.*?)"')
#         objURL = re.findall(patternt2,results)
#         for URL in tqdm(objURL,desc='\033[0;34;m正在下载...\033[0m《\033[0;32;m{}\033[0m》\033[0;34;m第{}页\033[0m'.format(word,int((index/20)+1))):
#             iname = parse_iamgeName(URL)
#             save_image(URL,iname,word)
#     except Exception as E:
#         print(E)
#         # print('请求网页异常')
# def parse_iamgeName(URL):
#     image_name = '.jpg'
#     if '.jpg' in URL:
#         image_name = '.jpg'
#     elif '.png' in URL:
#         image_name = '.png'
#     elif '.gif' in URL:
#         image_name = '.gif'
#     elif '.bmp' in URL:
#         image_name = '.bmp'
#     return image_name
# def save_image(url,iname,word):
#     try:
#         response = requests.get(url,timeout = 30)
#         if response.status_code == 200:
#             content = response.content #.content为了获取到图片的bytes格式文件
#             # 在当前目录创建文件夹
#             path = r'{0}\baodu_images\{1}'.format(os.getcwd(),word)
#             if not os.path.exists(path):
#                 os.makedirs(path)
#             # 创建md5文件名，方便检测文件的唯一性
#             file_path = path+'\{0}{1}'.format(md5(content).hexdigest(),iname)
#             if not os.path.exists(file_path):
#                 with open(file_path,'wb') as f:
#                     f.write(content)
#                     f.close()
#         else:
#             return None
#     except RequestException as E:
#         print('\n\033[0;31;m请求下载页面超时跳过:{}\033[0m'.format(url))
#
#
# def main(word,index):
#     get_imageURL(word,index)
#
# if __name__=='__main__':
#     word = input('\033[0;34;m请输入关键字:..\033[0m')
#     page = int(input('\033[0;34;m请输入想要爬取的页数:..\033[0m'))
#     print('爬虫运行开始:...{}'.format(time.ctime()))
#     start = time.time()
#     for i in range(page):
#         main(word,i*20)
#
#     print('爬虫运行结束:...{}'.format(time.ctime()))
#     end = time.time()
#     print('爬虫一共运行...{}秒'.format(end-start))
