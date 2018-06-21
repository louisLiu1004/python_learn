<<<<<<< HEAD
# coding: utf-8 
=======
# coding: utf-8
>>>>>>> origin/master
__author__ = '財'
__time__ = '2018/6/21 19:53'

__author__ = '財'

import json
import hashlib

user_name = []
users_info = {}
newusers_info = {}
users_info_amd = {'adm': '88888888'}


def info_read():
<<<<<<< HEAD
     f2 = open(r'name_info.md','r')
=======
     f2 = open(r'name_info.txt','r')
>>>>>>> origin/master

     for line in f2.readlines():
         data = json.loads(line)
         key, = data
         users_info[key] = data[key]

     f2.close()
     return users_info

def info_write():
<<<<<<< HEAD
    f = open('name_info.md','a')
=======
    f = open(r'name_info.txt','a')
>>>>>>> origin/master
    data = json.dumps(newusers_info)
    f.write(data + '\n')
    f.close()


def hash(pw):
    m = hashlib.md5()
    m.update(pw.encode('utf-8'))
    code = m.hexdigest()
    return code

login_status = ['F']
login_status_adm = ['F']

def sign_up():
    print('<>'*20,'欢迎注册','<>'*20)
    info_read()
    userinfo(input('输入用户名：'),input('输入6位数以上的密码：'))

def userinfo(user,pw):
    if user not in users_info.keys()and len(pw) > 6:
        newusers_info[user] =hash(pw)
        info_write()
        newusers_info.clear()
        print('注册成功')
        start()
    else:
        print('ERROR:用户名已经存在或密码小于6位数，请重新输入：')
        sign_up()


def Login_adm(func):
    def Tesing_():
        if login_status_adm[0] is 'F':
            user = input('管理员账号(区分大小写)：')
            password = input('管理员密码：')
            # hash_pw = hash(password)
            if user in users_info_amd.keys() and password == users_info_amd[user]:
                login_status_adm[0] = 'T'
                func()
            else:
                print('账户密码错误，重新输入')
                Tesing_()
        else:
            func()
    return Tesing_


def Login_(func):
    def Tesing_():
        if login_status[0] is 'F':
            info_read()
            user = input('用户名(区分大小写)：')
            password = input('密码：')
            hash_pw = hash(password)
            if user in users_info.keys() and hash_pw == users_info[user]:
                login_status[0] = 'T'
                func()
            else:
                print('账户密码错误，重新输入')
                Tesing_()
        else:
            func()
    return Tesing_

@Login_
def Home_page():
    print('欢迎来到首页')
    print('='*20)
<<<<<<< HEAD
    keys = input('0注册，1跳转到书店，2跳转到商店 3管理员登陆：')
=======
    keys = input('0注册，1跳转到书店，2跳转到商店 3管理员：')
>>>>>>> origin/master
    while True:
        if keys == '0':
            sign_up()
        elif keys == '1':
            Book()
        elif keys == '2':
            Shop()
        elif keys == '3':
            adm()
        else:
            print('输入有误，重新输入')
            keys = input('0返回首页，1跳转到书店，2跳转到商店：')

@Login_
def Book ():
    print('欢迎来到书城')
<<<<<<< HEAD
    keys = input('0返回首页，1管理员登陆，2跳转到商店：')
=======
    keys = input('0返回首页，1跳转到书店，2跳转到商店：')
>>>>>>> origin/master
    while True:
        if keys == '0':
            Home_page()
        elif keys == '1':
<<<<<<< HEAD
            adm()
=======
            Book()
>>>>>>> origin/master
        elif keys == '2':
            Shop()
        else:
            print('输入有误，重新输入')
            keys = input('0返回首页，1跳转到书店，2跳转到商店：')

@Login_
def Shop ():
    print('欢迎来到商店')
<<<<<<< HEAD
    keys = input('0返回首页，1跳转到书店，2管理员登陆：')
=======
    keys = input('0返回首页，1跳转到书店，2跳转到商店：')
>>>>>>> origin/master
    while True:
        if keys == '0':
            Home_page()
        elif keys == '1':
            Book()
        elif keys == '2':
<<<<<<< HEAD
            adm()
=======
            Shop()
>>>>>>> origin/master
        else:
            print('输入有误，重新输入')
            keys = input('0返回首页，1跳转到书店，2跳转到商店：')


@Login_adm
def adm():
    print('欢迎来到管理页面')
    keys = input('0、查看用户 2、删除用户： ')
    while True:
        if keys == '0':
            info_read()
            for key in users_info:
                 print('已经注册的用户名: %s' % key)
            keys = input('1、返回首页：')
        elif keys == '1':
            Home_page()
        else:
            print('输入有误，重新输入')
            keys = input('0、查看用户：')





if __name__ == '__main__':
<<<<<<< HEAD

    def file():
        f= open('name_info.md','a')
        f.close()

    file()

=======
>>>>>>> origin/master
    def start():
        print('*'*40)
        print('1、注册','2、首页登录','3、书店登录','4、商店登录','5、管理员登录')
        sel_num = input('请选择：')
        while True:
            if sel_num == '1':
                sign_up()
            elif sel_num == '2':
                Home_page()
            elif sel_num == '3':
                Book()
            elif sel_num == '4':
                Shop()
            elif sel_num == '5':
                adm()
            else:
                print('输入有误，重新输入')
<<<<<<< HEAD
                print('1、注册', '2、首页登录', '3、书店登录', '4、商店登录','5、管理员登录')
=======
                print('1、注册', '2、首页登录', '3、书店登录', '4、商店登录')
>>>>>>> origin/master
                sel_num = input('请选择：')
    start()