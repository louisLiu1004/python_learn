__author__ = '財'


user_name = []
users_info = {'louis':'123456','alex':'456789'}




login_status = ['F']

def sign_up():
    print('<>'*20,'欢迎注册','<>'*20)
    userinfo(input('输入用户名：'),input('输入6位数以上的密码：'))

def userinfo(user,pw):
    if user not in users_info.keys()and len(pw) > 6:
        users_info[user] =str(pw)
        print('注册成功')
        start()
    else:
        print('ERROR:用户名已经存在或密码小于6位数，请重新输入：')
        sign_up()


def Login_(func):
    def Tesing_():
        if login_status[0] is 'F':
            user = input('用户名(区分大小写)：')
            password = input('密码：')
            if user in users_info.keys() and password == users_info[user]:
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
    keys = input('0返回首页，1跳转到书店，2跳转到商店：')
    while True:
        if keys == '0':
            Home_page()
        elif keys == '1':
            Book()
        elif keys == '2':
            Shop()
        else:
            print('输入有误，重新输入')
            keys = input('0返回首页，1跳转到书店，2跳转到商店：')

@Login_
def Book ():
    print('欢迎来到书城')
    keys = input('0返回首页，1跳转到书店，2跳转到商店：')
    while True:
        if keys == '0':
            Home_page()
        elif keys == '1':
            Book()
        elif keys == '2':
            Shop()
        else:
            print('输入有误，重新输入')
            keys = input('0返回首页，1跳转到书店，2跳转到商店：')

@Login_
def Shop ():
    print('欢迎来到商店')
    keys = input('0返回首页，1跳转到书店，2跳转到商店：')
    while True:
        if keys == '0':
            Home_page()
        elif keys == '1':
            Book()
        elif keys == '2':
            Shop()
        else:
            print('输入有误，重新输入')
            keys = input('0返回首页，1跳转到书店，2跳转到商店：')



if __name__ == '__main__':
    def start():
        print('*'*40)
        print('1、注册','2、首页登录','3、书店登录','4、商店登录')
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
            else:
                print('输入有误，重新输入')
                print('1、注册', '2、首页登录', '3、书店登录', '4、商店登录')
                sel_num = input('请选择：')
    start()