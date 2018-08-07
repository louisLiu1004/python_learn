# get方式向网站发送请求
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# post方式向网站发送请求
# import urllib.request
# import urllib.parse
# data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())

# 设置超时时间
# import urllib.request
# response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
# print(response.read().decode('utf-8'))


# 超时异常处理
# import urllib.request
# import socket
# import  urllib.error
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')

# 响应类型
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(type(response)) #<class 'http.client.HTTPResponse'>


#获取状态码、响应头
# import urllib.request
# response = urllib.request.urlopen('https://www.python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

# Request参数
# from urllib import request,parse
# url = 'http://www.httpbin.org/post'
# headers = {'User-Agent':'Mozilla/4.0 (compatible;MSIE 5.5;Window NT)','Host':'httpbin.org'}
# dict = {'name':'Germay'}
# data = bytes(parse.urlencode(dict),encoding='utf8')
# req = request.Request(url=url,data=data,headers=headers,method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

# 代理
# import urllib.request
# proxy_handler = urllib.request.ProxyHandler({'http':'http://127.0.0.1:25378','https':'https://127.0.0.1:25378'})
# opener = urllib.request.build_opener(proxy_handler)
# response = opener.open('http://www.httpbin.org/get')
# print(response.read().decode('utf-8'))

# Cookie
# import http.cookiejar,urllib.request
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+' = '+item.value)

# 保存cookie文件
# import http.cookiejar,urllib.request
# # file = 'cookie.txt'
# # cookie = http.cookiejar.MozillaCookieJar(file)
# # handler = urllib.request.HTTPCookieProcessor(cookie)
# # opener = urllib.request.build_opener(handler)
# # response = opener.open('http://www.baidu.com')
# # cookie.save(ignore_discard=True,ignore_expires=True)

# 加载cookie文件
# import http.cookiejar,urllib.request
# cookie = http.cookiejar.MozillaCookieJar()
# cookie.load('cookie.txt',ignore_expires=True,ignore_discard=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# url解析
# from urllib.parse import urlparse
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result),result)

# urlunpares
# from urllib.parse import urlunparse
# data = ['http','www.baidu.com','index.html','user','id=5','comment']
# print(urlunparse(data))

# urljoin
# from urllib.parse import urljoin
# print(urljoin('http://www.baidu.com','FAQ.html'))
# print(urljoin('http://www.baidu.com','https://www.louis.com'))

# urlencode
# from urllib.parse import urlencode
# params = {'name':'germay','age':'22'}
# base_url = 'http://www.baidu.com?'
# url = base_url+urlencode(params)
# print(url)
#
