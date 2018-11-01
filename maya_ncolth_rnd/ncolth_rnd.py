# -*- coding: utf-8 -*-
"""
@author: 刘国财
@software: PyCharm 2018.1
@file: ncolth_rnd.py
@time: 2018/10/30 11:09
"""

from Qt import QtWidgets, QtCompat, QtCore
import Tools
import maya.cmds as mc
import os
import file_handle

reload(file_handle)


class MyWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWin, self).__init__()
        QtCompat.loadUi(r'J:\python\python_learn\maya_ncolth_rnd\ui\ncloth_rnd.ui', self)
        self.step = self.step_spinbox.value()
        self.attr = []
        self.info = []
        self.shape_node = mc.ls(typ='nCloth')
        self.comboBox.addItems(self.shape_node)
        self.simlate = Simlaution()
        self.simlate.signal.connect(self.update_process)
        self.actionExit.triggered.connect(self.close)
        self.get_path_button.clicked.connect(self.get_path)
        self.run_button.clicked.connect(self.connect_to_sim)

    def get_path(self):
        dirs = QtWidgets.QFileDialog.getExistingDirectory(self, u'选择路径', Tools.get_project_path())
        return self.set_path(dirs)

    def set_path(self, dirs):
        self.path_line_edit.setText(dirs)

    def get_attr(self, info):
        print(u'获取初始化值成功')
        self.step = self.step_spinbox.value()
        for lists in info:
            name = lists[0]
            min_ = float(lists[1])
            max_ = float(lists[2])
            self.attr += (min_, max_)
            sub_step = (max_ - min_) / self.step
            for i in range(self.step - 1):
                self.attr.append(min_ + (sub_step * (i + 1)))
            self.simlate.action(self.comboBox.currentText(), self.path_line_edit.text().replace('/', '\\'), name,
                                self.attr, len(info))
            self.attr = []
        self.simlate.count = 0

    def connect_to_sim(self):
        if self.rnd_process.value() != 0:
            self.rnd_process.setValue(0)
        for i in range(20):
            checkbox = getattr(self, 'b%d' % i)
            if checkbox.checkState():
                name = getattr(self, 'l%d' % i)
                min_attr = getattr(self, 'min_%d' % i)
                max_attr = getattr(self, 'max_%d' % i)
                if not min_attr.text():
                    mc.warning(name.text() + u'最小值不能为空')
                    self.info = []
                    return
                elif not max_attr.text():
                    mc.warning(name.text() + u'# 最大值不能为空')
                    self.info = []
                    return
                elif not self.path_line_edit.text():
                    mc.warning(name.text() + u'# 路径不能为空')
                    self.info = []
                    return
                elif not self.comboBox.currentText():
                    mc.warning(name.text() + u'# 请确认相应的粒子节点')
                    self.info = []
                    return
                else:
                    try:
                        float(min_attr.text())
                        float(max_attr.text())
                        if [name.text(), min_attr.text(), max_attr.text()] not in self.info:
                            self.info.append([name.text(), min_attr.text(), max_attr.text()])
                    except ValueError:
                        mc.warning(u'请输入正确的数字')
                        self.info = []
                        return
        self.get_attr(self.info)
        self.info = []

    def update_process(self, value):
        self.rnd_process.setValue(value)
        # 如果100，完成
        if self.rnd_process.value() == 100:
            return


class Simlaution(QtCore.QThread):
    signal = QtCore.Signal(int)

    def __init__(self):
        super(Simlaution, self).__init__()
        self.count = 0

    def action(self, node, path, attr_name, attrs, length):
        deafult_attr = mc.getAttr(node + '.' + attr_name)
        for attr in attrs:
            mc.setAttr(node + '.' + attr_name, attr)
            file_path = path + '/' + attr_name + '_' + str(round(attr, 4)) + '/' + attr_name + '_' + str(
                round(attr, 4)) + '_'
            folder = attr_name + '_' + str(round(attr, 4))
            if not os.path.exists(os.path.join(path, folder)):
                mc.playblast(format="image", filename=file_path, compression="png", percent=100, viewer=False,
                             wh=[mc.getAttr("defaultResolution.width"), mc.getAttr("defaultResolution.height")],
                             fo=True)
                file_handle.file_save(os.path.join(path, folder), node)
            else:
                file_handle.file_check(os.path.join(path, folder), folder)
                mc.playblast(format="image", filename=file_path, compression="png", percent=100, viewer=False,
                             wh=[mc.getAttr("defaultResolution.width"), mc.getAttr("defaultResolution.height")],
                             fo=True)
                file_handle.file_save(os.path.join(path, folder), node)
            self.count += 1.0
            self.signal.emit(int((self.count / (len(attrs) * length)) * 100))
        mc.setAttr(node + '.' + attr_name, deafult_attr)
