# 实战案例
import requests
import re
rep = requests.get('http://www.cbooo.cn/').text
parrent = re.compile('<td\sstyle.*?150px\'>(.*?)</td>.*?120px\'>(.*?)</td>.*?120px\'>(.*?)</td>.*?70px;\'>(.*?)</td>.*?</tr>',re.S)
results = re.findall(parrent,rep)
i = 1
for result in results:
    name,real,booking,days = result
    name = re.sub('\s','',name)
    real = re.sub('\s','',real)
    booking = re.sub('\s','',booking)
    days = re.sub('\s','',days)
    print('{0} \033[0;34;m影片名字：\033[0m {1} \033[0;32;m实时票房:\033[0m {2}万 \033[0;31;m累计票房:\033[0m {3}万 \033[0;33;m上映天数:\033[0m {4}'.format(i,name,real,booking,days))
    i+=1