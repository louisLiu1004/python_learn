import requests
from bs4 import BeautifulSoup
import re
import subprocess

base_url = 'https://www.youtube.com/watch?v='
url = []
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
        'x-client-data': 'CI62yQEIpLbJAQjBtskBCKmdygEI2J3KAQjancoBCKijygE='
    }
totalVideo = re.compile('"ytInitialData.*?totalVideos.*?:(\d+),"ownerName"', re.S)
videoIds = re.compile('"watchEndpoint":{"videoId":"(.*?)",', re.S)
list_patten = re.compile('list=(.*?)$',re.S)
ids = []
downUrl = []
def parser_html(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            Bsp = BeautifulSoup(response.text, 'html.parser')
            scripts = Bsp.select('script')
            for script in scripts:
                if 'watchEndpoint'in script.text:
                    str = script.text.strip()
                    return str
    except requests.RequestException as e:
        return 0

def total_index(str):
    try:
        nums = re.findall(totalVideo, str)
        return int(nums[0])
    except Exception as e:
        print(e)

def video_ID(str):
    global ids
    try:
        id = re.findall(videoIds,str)
        for i in id:
            if i not in ids and len(i) < 12:
                ids.append(i)
    except Exception as e:
        print(e)

def main(url):
    global ids
    str = parser_html(url)
    video_ID(str)
    nums = total_index(str)
    if nums/79.0>1:
        list_id = re.findall(list_patten,url)[0]
        for i in range(int(nums/79.0)):
            len_list = len(ids)
            new_url = 'https://www.youtube.com/watch?v={0}&index={1}&list={2}'.format(ids[int(len_list)-1],int(len_list)-4,list_id)
            str = parser_html(new_url)
            video_ID(str)

    for id in ids:
        downUrl.append(base_url+id)
    print('begin download')
    try:
        for down in downUrl:
            action = subprocess.Popen('youtube-dl -c  '+down, shell=True, stdout=subprocess.PIPE)
            print(action.stdout.read().decode('utf-8'))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    url = input('please input youtube list url :  ')
    main(url)
