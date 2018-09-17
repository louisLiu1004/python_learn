# -*- coding: utf-8 -*-

import requests
import os
import re
import urllib as up
import hashlib
import math
import sys
from PySide.QtGui import QApplication,QWidget,QFileDialog
from ui.baidu_image import Ui_Form

class baidu(Ui_Form,QWidget):
    def __init__(self,parent = None):
        super(baidu, self).__init__(parent)
        self.count = 0
        self.setupUi(self)
        self.go.clicked.connect(self.main)
        self.get_path.clicked.connect(self.set_path)
    def set_path(self):
        dir1 = QFileDialog.getExistingDirectory(self)
        self.path_edit.setText(dir1)

    def main(self):
        word = self.key_Edit.text()
        index = int(self.page_edit.text().encode('utf-8'))
        word = word.encode('utf-8')
        if index < 3:
            for i in range(2):
                self.get_imageURL(word,index*60)
        else:
            for i in range(int(math.ceil(index/3))):
                self.get_imageURL(word,index*60)

    def get_imageURL(self,word,index):
        headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
            }

        try:
            response = requests.get('https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={0}&pn={1}'.format(up.quote(word),index),headers=headers).text
            patternt = re.compile('flip.setData.*?imgData\'.*?{}]}\)')
            results = re.search(patternt,response).group()
            patternt2 = re.compile('"objURL":"(.*?)"')
            objURL = re.findall(patternt2,results)
            if len(objURL)>0:
                for URL in objURL:
                    URL = URL.encode('utf-8')
                    iname = self.parse_iamgeName(URL)
                    self.save_image(URL,iname,word)
                    self.count+=1
                    self.progressBar.setValue(self.count/int(len(objURL))*100)
            else:
                 print('《\033[0;32;m{}\033[0m》None\033[0;34;mPage{}-{}\033[0m'.format(word,int((index/20)+1),int((index/20)+3)))
            print('final')
        except Exception as E:
            print('i am get_imageURL')
            print(E)

    def parse_iamgeName(self,URL):
        image_name = '.jpg'
        if '.jpg' in URL:
            image_name = '.jpg'
        elif '.png' in URL:
            image_name = '.png'
        elif '.gif' in URL:
            image_name = '.gif'
        elif '.bmp' in URL:
            image_name = '.bmp'
        return image_name

    def save_image(self,url, iname, word):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                content = response.content
                path_edit = self.path_edit.text()
                path2 = path_edit.encode('utf-8')
                path = path2+'\{0}'.format(word)
                if not os.path.exists(path):
                    os.makedirs(path)

                file_path = path + '\{0}{1}'.format(hashlib.md5(content).hexdigest(), iname)
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(content)
                        f.close()
            else:
                return None
        except requests.RequestException as E:
            path_edit_ERROR = self.path_edit.text()
            path2_ERROR = path_edit_ERROR.encode('utf-8')
            path_ERROR = path2_ERROR + '\{0}'.format(word)
            path3 = path_ERROR+'\Timeout.txt'
            with open(path3, 'a') as f:
                f.write('TimeOut:' + url + '\n')
                f.close()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    qwidget = baidu()
    qwidget.show()
    sys.exit(app.exec_())


