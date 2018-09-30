# coding: utf-8 
__author__ = '財'
__time__ = '2018/9/30 22:00'

# -*- coding: utf-8 -*-
from wxpy import *
import time

# 启动机器人，console_qr=True是命令行二维码，改False是图片二维码
bot = Bot(cache_path=True, console_qr=True)
# 获取所有好友
chats = bot.friends(update=True)
# 排除指定好友
chats.remove(chats.search(u'妈')[0])
chats.remove(chats.search(u'爸爸')[0])
# 启动和退出关键字，添加规则 （,'关键字'）
start = [u'启动', u'开始', u'激活', u'回来', u'上线', 'Q']
stop = [u'退下', u'退出', u'滚', u'下线', u'离开', u'关闭', 'T']
config = {}


class NewTuling(Tuling):
    def __init__(self):
        # 图灵api
        super(NewTuling, self).__init__(api_key='你的图灵api')

    # 自动回复方法
    def do_reply(self, msg, at_member=False):
        ret = self.reply_text(msg, at_member)
        ret = ret + u'\n @来自财哥人工智能'
        msg.reply(ret)
        return ret

    # 首次启动方法
    def first(self, msg):
        # 欢迎词，随意更改
        ret = u'主人可能不在，默认进入智能聊天模式！  \n\n回复T退出'
        msg.reply(ret)
        return ret

    # 启动回复
    def dostart(self, msg):
        ret = u'财哥的人工智能已启动 \n回复T退出'
        msg.reply(ret)
        return ret

    # 停止回复
    def dostop(self, msg):
        ret = u'财哥的人工智能已停止 \n回复Q退出'
        msg.reply(ret)
        return ret


# 配置函数，保存每个好友退出和启动状态，字典格式
def conf(chat, num):
    global config
    config[chat] = num
    return config


# 注册会话，监听消息
@bot.register(chats)
def reply_my_friend(msg):
    # 判断是否是群，群聊自动忽略，不参与
    if isinstance(msg.chat, Group):
        return
    else:
        # 判断是否是启动
        if msg.text in start:
            conf(msg.chat, 1)
            tuling.dostart(msg)
            return
        # 判断是否是停止
        elif msg.text in stop:
            conf(msg.chat, 0)
            tuling.dostop(msg)
            return
    try:
        # 获取好友配置信息，启动则自动回复消息
        if config[msg.chat]:
            time.sleep(3)
            tuling.do_reply(msg)
        else:
            return
    except KeyError:
        # 获取不到配置消息，则默认启动并自动回复欢迎词
        conf(msg.chat, 1)
        time.sleep(3)
        tuling.first(msg)


if __name__ == '__main__':
    tuling = NewTuling()
    embed()


