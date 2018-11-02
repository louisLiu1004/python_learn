# coding=UTF-8
import requests
import re
import sys
from python_learn import booking
from PySide.QtGui import QWidget,QApplication


class booking_office(booking.Ui_Form, QWidget):
    def __init__(self,parent = None):
        super(booking_office,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u'票房排行榜')
        self.pushButton.clicked.connect(self.clean)

    def clean(self):
        self.textBrowser.setText('')
        self.booking_claw()

    def booking_claw(self):
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
            if not float(booking)/10000 >=1:
                self.textBrowser.append(u'{0} 影片名字：{1} 实时票房:{2}万 累计票房:{3}万 上映天数:{4}'.format(i,name,real,booking,days)+'\n')
            else:
                self.textBrowser.append(u'{0} 影片名字：{1} 实时票房:{2}万 累计票房:{3}亿 上映天数:{4}'.format(i, name, real, (float(booking)/10000), days)+'\n')
            i+=1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = booking_office()
    widget.show()
    sys.exit(app.exec_())


