# coding: utf-8 
__author__ = '財'
__time__ = '2018/9/17 20:53'

# 导入time,os,shutil,sys模块
import time, os, shutil, sys
from organizeFileUi import Ui_Form  # 导入UI文件
from PySide import QtCore
from PySide.QtGui import QWidget, QApplication, QFileDialog

source_path = ''
data_time = None


# 链接界面UI
class OrganizeFileUiConnect(Ui_Form, QWidget):
    def __init__(self):
        super(OrganizeFileUiConnect, self).__init__()
        self.setupUi(self)
        global data_time
        # 获取初始时间
        data_time = time.mktime(time.strptime(self.dateEdit.text(), '%Y/%m/%d'))
        # 设置按钮链接
        self.set_path.clicked.connect(self.get_path)
        self.dateEdit.dateChanged.connect(self.set_datatime)
        self.Go.clicked.connect(self.main)

    def update_process(self, value):
        self.progressBar.setValue(value)
        if self.progressBar.value() == 100:
            self.complete_info.setText(u'整理完成')

    def get_path(self):
        # 设置整理的原始路径
        global source_path
        source_path = QFileDialog.getExistingDirectory(self)
        self.path_edit.setText(source_path

    def set_datatime(self):
        # 获取条件的时间戳格式
        global data_time
        data_time = time.mktime(time.strptime(self.dateEdit.text(), '%Y/%m/%d')

    def main(self)
        self.begin_organize = Organizefile()
        self.begin_organize.signal.connect(self.update_process)
        self.begin_organize.action()


class Organizefile(OrganizeFileUiConnect, QtCore.QThread):
    signal = QtCore.Signal(int)

    def __init__(self):
        super(Organizefile, self).__init__()

    def action(self):
        # 列出路径所有文件：
        count = 0
        file_names = []
        for file in os.listdir(source_path):
            # 获取文件完整路径
            source_dir = os.path.join(source_path, file)
            # 判断是不是文件：
            if os.path.isfile(source_dir):
                # 把所有文件添加到列表，方便获取数量
                file_names.append(file)
        # 遍历文件
        for file_name in file_names:
            file_dir = os.path.join(source_path, file_name)
            # 获取文件修改时间
            file_modify_time = os.path.getmtime(file_dir)
            # 判断文件修改时间>条件时间
            if file_modify_time > data_time:
                # 创建新文件路径
                new_path = os.path.join(source_path, 'new')
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                target_path = os.path.join(new_path, file_name)
            else:
                # 创建旧文件路径
                old_path = os.path.join(source_path, 'old')
                if not os.path.exists(old_path):
                    os.makedirs(old_path)
                target_path = os.path.join(old_path, file_name)
            # 移动文件到相对应的文件夹
            shutil.move(file_dir, target_path)
            count += 1.0
            self.signal.emit(int((count / len(file_names)) * 100))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qwidget = OrganizeFileUiConnect()
    qwidget.show()
    app.exit(app.exec_())
