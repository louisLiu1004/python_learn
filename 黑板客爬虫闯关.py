
# 第一关
# from bs4 import BeautifulSoup
# import requests
# import re
# import time
#
# url = 'http://www.heibanke.com/lesson/crawler_ex00/'
# print('爬虫闯关开始...{}'.format(time.ctime()))
# while 1:
#     print('访问页面...{}'.format(url))
#     response = requests.get(url).text
#     soup = BeautifulSoup(response,'html.parser')
#     massages = soup.select('h3')
#     print(massages[0].text)
#     num = re.findall('\d+',massages[0].text)
#     if num == []:
#         print('闯关成功...{}'.format(time.ctime()))
#         break
#     else:
#         url = 'http://www.heibanke.com/lesson/crawler_ex00/'+ num[0]


# 第二关

# import requests
#
# url = 'http://www.heibanke.com/lesson/crawler_ex01/'
# datas = {'username':'louis','password':'1'}
# for i in range(31):
#     datas['password'] = i
#     print('传入的参数...{}'.format(datas))
#     response = requests.post(url,data=datas)
#     if '成功'in response.text:
#         print('闯关成功...{}'.format(datas))
#         break
#     else:
#         print('继续努力....')

# 第三关
# import requests
#
# url = 'http://www.heibanke.com/lesson/crawler_ex02/'
# login_url = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'
# login_data = {'username':'louis','password':'123456'}
#
#
# response = requests.get(login_url)
# cookies = response.cookies# 获取未登录时候cookies
#
# login_data['csrfmiddlewaretoken']=cookies['csrftoken']
# login_response = requests.post(login_url,allow_redirects=False,data=login_data,cookies=cookies) #allow_redirects不允许重定向
# #因为要获取登录成功状态的cookies，在下次打开url时候，知道用户已经登录，然后跳转到真正的测试页面
# login_cookies = login_response.cookies# 获取登录成功的cookies
#
# guess_data ={'username':'louis','password':'1','csrfmiddlewaretoken':login_cookies['csrftoken']}
# for i in range(31):
#     guess_data['password']=i
#     print('尝试登录密码..{}'.format(guess_data['password']))
#     guess_result = requests.post(url,data=guess_data,cookies=login_cookies)
#     if '成功' in guess_result.text:
#         print('\033[0;32;m登录成功密码....{}\033[0m'.format(guess_data['password']))
#         break
#     else:
#         print('\033[0;31;m继续努力.....\033[0m')



# 第四关，单线程
# import requests
# import re
# import time
#
# def login(login_url):
#     response = requests.get(login_url)
#     cookies = response.cookies# 获取未登录时候cookies
#     login_data['csrfmiddlewaretoken']=cookies['csrftoken']
#     login_response = requests.post(login_url,allow_redirects=False,data=login_data,cookies=cookies) #allow_redirects不允许重定向
#     #因为要获取登录成功状态的cookies，在下次打开url时候，知道用户已经登录，然后跳转到真正的测试页面
#     login_cookies = login_response.cookies# 获取登录成功的cookies
#     return login_cookies
#
# def guess(parrent_pos,parrent_val,login_cookies):
#     global passwords
#     while 1 :
#         rep = requests.get('http://www.heibanke.com/lesson/crawler_ex03/pw_list/?page=1',cookies=login_cookies)
#         print('响应状态码:{}'.format(rep.status_code))
#         response = rep.text
#         pos = re.findall(parrent_pos,response)
#         vals = re.findall(parrent_val,response)
#         for i in range(len(pos)):
#             passwords[int(pos[i])-1]=(vals[i])
#         if '' in passwords:
#             print('获取到密码:{}'.format(int(''.join(passwords))))
#         else:
#             int_pass = int(''.join(passwords))
#             break
#     return int_pass
#
# def main(url,login_url):
#     parrent_pos = re.compile('td\s.*?password_pos\">(\d+)</td>')
#     parrent_val = re.compile('td\s.*?password_val\">(\d+)</td>')
#     print(time.ctime())
#     login_cookies = login(login_url)
#     print('\033[0;32;m成功连线\033[0m')
#     int_pass = guess(parrent_pos,parrent_val,login_cookies)
#     print('\033[0;31;m拿到密码尝试登录.................\033[0m')
#     while 1:
#         guess_data = {'username':'louis','password':int_pass,'csrfmiddlewaretoken':login_cookies['csrftoken']}
#         login_ = requests.post(url,data=guess_data,cookies=login_cookies)
#         if '成功' in login_.text:
#             print('\033[0;32;m登录成功密码....{}\033[0m'.format(int_pass))
#             break
#         else:
#             print('\033[0;31;m继续努力.....\033[0m')
#             int_pass = guess(parrent_pos, parrent_val, login_cookies)
#     print(time.ctime())
#
# if __name__== '__main__':
#     url = 'http://www.heibanke.com/lesson/crawler_ex03/'
#     login_url = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex03/'
#     login_data = {'username': 'louis', 'password': '123456'}
#     passwords = ['' for i in range(100)]
#     main(url,login_url)

# 第四关，多线程

import requests
import re
import time
import threading
def login(login_url):
    response = requests.get(login_url)
    cookies = response.cookies# 获取未登录时候cookies
    login_data['csrfmiddlewaretoken']=cookies['csrftoken']
    login_response = requests.post(login_url,allow_redirects=False,data=login_data,cookies=cookies) #allow_redirects不允许重定向
    #因为要获取登录成功状态的cookies，在下次打开url时候，知道用户已经登录，然后跳转到真正的测试页面
    login_cookies = login_response.cookies# 获取登录成功的cookies
    return login_cookies



class MyThread(threading.Thread):
    def __init__(self ,func ,args=()):
        super(MyThread ,self).__init__()
        self.func = func
        self.args = args
    def run(self):
        self.result = self.func(*self.args)
    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def guess(parrent_pos,parrent_val,login_cookies):
    global passwords
    while 1 :
        rep = requests.get('http://www.heibanke.com/lesson/crawler_ex03/pw_list/?page=1',cookies=login_cookies)
        print('\033[0;32;m响应状态码:{}\033[0m'.format(rep.status_code))
        response = rep.text
        pos = re.findall(parrent_pos,response)
        vals = re.findall(parrent_val,response)
        for i in range(len(pos)):
            passwords[int(pos[i])-1]=(vals[i])
        if '' in passwords:
            print(threading.current_thread().getName(),'  获取到密码:{}'.format(''.join(passwords)))
        else:
            int_pass = int(''.join(passwords))
            break
    return int_pass

def main(url,login_url):
    parrent_pos = re.compile('td\s.*?password_pos\">(\d+)</td>')
    parrent_val = re.compile('td\s.*?password_val\">(\d+)</td>')
    print(time.ctime())
    start = time.time()
    login_cookies = login(login_url)
    print('\033[0;32;m成功连线\033[0m')
    li = []
    for i in range(2):
        t = MyThread(guess, args=(parrent_pos,parrent_val,login_cookies))
        li.append(t)
        t.start()
    for t in li:
        t.join()  # 一定要join，不然主线程比子线程跑的快，会拿不到结果
    int_pass = t.get_result()
    print('get the password.....尝试登陆..............')
    while 1:
        guess_data = {'username':'louis','password':int_pass,'csrfmiddlewaretoken':login_cookies['csrftoken']}
        login_ = requests.post(url,data=guess_data,cookies=login_cookies)
        if '成功' in login_.text:
            end =time.time()
            print('\033[0;32;m登录成功密码....{}\033[0m'.format(guess_data))
            print('\033[0;32;m总共运行时间....{}\033[0m'.format(end-start))
            break
        else:
            print('\033[0;31;m继续努力.....\033[0m')
            int_pass = guess(parrent_pos, parrent_val, login_cookies)
    print(time.ctime())

if __name__== '__main__':
    url = 'http://www.heibanke.com/lesson/crawler_ex03/'
    login_url = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex03/'
    login_data = {'username': 'louis', 'password': '123456'}
    passwords = ['' for i in range(100)]
    main(url,login_url)


