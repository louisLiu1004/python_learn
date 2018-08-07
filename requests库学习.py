# 简单实例
# import requests
# response = requests.get('http://httpbin.org/get')
# print(response.text)

# 各种请求方式
import requests
# print(requests.options('http://httpbin.org/get'))
# print(requests.post('http://httpbin.org/post'))
# print(requests.put('http://httpbin.org/put'))
# print(requests.delete('http://httpbin.org/delete'))
# print(requests.head('http://httpbin.org/get'))

# 带参数get请求
# import requests
# response = requests.get('http://httpbin.org/get?name=louis&age=22')
# print(response.text)

# import requests
# params = {'name':'louis','age':'22'}
# response = requests.get('http://httpbin.org/get',params=params)
# print(response.text)

# 获取二进制数据并保存
# import requests
# # response = requests.get('https://github.com/favicon.ico')
# # print(response.content)
# # with open('favicon.ico','wb')as f:
# #     f.write(response.content)
# #     f.close()

# 添加headers
# import requests
# header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# response = requests.get('https://www.zhihu.com/explore',headers = header)
# print(response.text)

# 基础post请求
# import requests
# data = {'name':'louis','age':'23'}
# response = requests.post('http://httpbin.org/post',data=data)
# print(response.text)

# 响应属性
# import requests
# response = requests.get('http://www.jianshu.com')
# print(type(response.status_code),response.status_code)
# print(type(response.headers),response.headers)
# print(type(response.cookies),response.cookies)
# print(type(response.url),response.url)
# print(type(response.history),response.history)

# 状态码判断
# import requests
# response = requests.get('https://www.baidu.com')
# if response.status_code == 200:
#     print('Successfully')
# else:
#     exit()

# 高级操作
# 文件上传
# import requests
# files = {'file':open('favicon.ico','rb')}
# response = requests.post('http://httpbin.org/post',files=files)
# print(response.text)

# 获取cookie
# import requests
# response = requests.get('https://www.baidu.com')
# for key,value in response.cookies.items():
#     print(key +' = '+ value)

# 会话维持，模拟登录
# import requests
# s = requests.session()
# s.get('http://httpbin.org/cookies/set/number/1234567')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)

# 证书验证
# import requests
# response = requests.get('https://www.12306.cn',verify = False)
# print(response.status_code)
#排除不验证证书的警告信息
# import requests
# import urllib3
# urllib3.disable_warnings()
# response = requests.get('https://www.12306.cn',verify = False)
# print(response.status_code)

# 代理
# import requests
# proxies = {'http':'http://127.0.0.1:25378','https':'https://127.0.0.1:25378'}
# response = requests.get('http://httpbin.org/get',proxies=proxies)
# print(response.text)

# 超时
# import requests
# # from requests.exceptions import ReadTimeout
# # try:
# #     response = requests.get('https://www.baidu.com',timeout=0.01)
# #     print(response.status_code)
# # except ReadTimeout :
# #     print('timeout')

# 登录认证，传输用户名和密码
# import requests
# # from requests.auth import HTTPBasicAuth
# response = requests.get('https://www.tiantianlouis.ml',auth=('louis','1993lgc1004'))
# print(response.status_code)

# 异常处理
# import requests
# from requests.exceptions import ReadTimeout,HTTPError,RequestException
# try:
#     response = requests.get('http://httpbin.org/get',timeout=0.2)
#     print(response.status_code)
# except ReadTimeout:
#     print('Timeout')
# except HTTPError:
#     print('HTTPError')
# except RequestException:
#     print('Error')