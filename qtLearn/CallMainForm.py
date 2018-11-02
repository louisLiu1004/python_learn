# -*- coding: utf-8 -*-
"""
@author: 刘国财
@software: PyCharm 2018.1
@file: CallMainForm.py
@time: 2018/10/18 17:48
"""

from PySide.QtGui import QApplication, QMainWindow, QFileDialog
from MainForm import Ui_MainWindow
import sys


class MyMainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWin, self).__init__()
        self.setupUi(self)
        self.actionClose.triggered.connect(self.close)
        self.actionOpen.triggered.connect(self.openMsg)

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, u'打开', 'C:/', 'ALL Files (*);;Text Files (*.txt)')
        self.statusbar.showMessage(file)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    win = MyMainWin()
    win.show()
    sys.exit(app.exec_())
