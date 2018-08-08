
# 常规匹配
# import re
# content= 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}.*$',content)
# print(result)
# print(result.group())
# print(result.span())

# 泛匹配
# import re
# content= 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello.*Regex',content)
# print(result)
# print(result.group())
# print(result.span())

# 获取匹配目标
# import re
# content= 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld.*Demo$',content)
# print(result)
# print(result.group(1))
# print(result.span())

# 贪婪匹配
# import re
# content= 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^H.*(\d+).*Demo$',content)
# print(result)
# print(result.group(1))

# 非贪婪匹配
# import re
# content= 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^H.*?(\d+).*Demo$',content)
# print(result)
# print(result.group(1))

# 匹配模式，有换行符要用re.S让.指定所有字符
# import re
# content= 'Hello 1234567 World_This ' \
#          'is a Regex Demo'
# result = re.match('^H.*?(\d+).*Demo$',content,re.S)
# print(result)
# print(result.group(1))

# re.search,能用search就用search
# import re
# content= 'Exit Hello 1234567 World_This is a Regex Demo happy'
# result = re.search('H.*?(\d+).*Demo',content)
# print(result)
# print(result.group(1))


# 实战案例

# import requests
# import re
# import time
#
# def crew_data(pattern,rep):
#     results = re.findall(pattern, rep)
#     return results
# def _main():
#     print(time.ctime())
#     rep = requests.get('https://book.douban.com').text
#     pattern = re.compile(
#         '<div\sclass="title">.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?publisher">(.*?)</span>',
#         re.S)
#     results = crew_data(pattern,rep)
#     for result in results:
#         url, name, author, year, publisher = result
#         name = re.sub('\s', '', name)
#         author = re.sub('\s', '', author)
#         year = re.sub('\s', '', year)
#         publisher = re.sub('\s', '', publisher)
#         print(url, '书名:', name, '作者:', author, '发行日期:', year, '出版社:', publisher)
#     print(time.ctime())
# if __name__ == '__main__':
#     _main()



# 实战案例
# import requests
# import re
# rep = requests.get('http://www.cbooo.cn/').text
# parrent = re.compile('<td\sstyle.*?150px\'>(.*?)</td>.*?120px\'>(.*?)</td>.*?120px\'>(.*?)</td>.*?70px;\'>(.*?)</td>.*?</tr>',re.S)
# results = re.findall(parrent,rep)
# i = 1
# for result in results:
#     name,real,booking,days = result
#     name = re.sub('\s','',name)
#     real = re.sub('\s','',real)
#     booking = re.sub('\s','',booking)
#     days = re.sub('\s','',days)
#     print('{0} \033[0;34;m影片名字：\033[0m {1} \033[0;32;m实时票房:\033[0m {2}万 \033[0;31;m累计票房:\033[0m {3}万 \033[0;33;m上映天数:\033[0m {4}'.format(i,name,real,booking,days))
#     i+=1
