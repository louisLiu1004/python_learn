# coding=UTF-8
import sys
from PySide.QtGui import QApplication,QWidget
import HelloUi

class Hello(HelloUi.Ui_Form,QWidget):
    def __init__(self,parent=None):
        super(Hello,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        self.textBrowser.append('Welcome '+self.lineEdit.text())
#
#
#
if __name__ == '__main__':

    app = QApplication(sys.argv)
    widget = Hello()
    widget.show()
    sys.exit(app.exec_())
