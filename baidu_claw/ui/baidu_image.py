# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baidu_image.ui'
#
# Created: Fri Sep 14 16:40:39 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(419, 163)
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(40, 110, 361, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.go = QtGui.QPushButton(Form)
        self.go.setGeometry(QtCore.QRect(330, 10, 75, 71))
        self.go.setObjectName("go")
        self.get_path = QtGui.QPushButton(Form)
        self.get_path.setGeometry(QtCore.QRect(280, 60, 31, 21))
        self.get_path.setObjectName("get_path")
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 10, 181, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.key_label = QtGui.QLabel(self.widget)
        self.key_label.setObjectName("key_label")
        self.horizontalLayout.addWidget(self.key_label)
        self.key_Edit = QtGui.QLineEdit(self.widget)
        self.key_Edit.setObjectName("key_Edit")
        self.horizontalLayout.addWidget(self.key_Edit)
        self.widget1 = QtGui.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(230, 10, 77, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.page_label = QtGui.QLabel(self.widget1)
        self.page_label.setObjectName("page_label")
        self.horizontalLayout_2.addWidget(self.page_label)
        self.page_edit = QtGui.QLineEdit(self.widget1)
        self.page_edit.setObjectName("page_edit")
        self.horizontalLayout_2.addWidget(self.page_edit)
        self.widget2 = QtGui.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(20, 60, 241, 22))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(self.widget2)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.path_edit = QtGui.QLineEdit(self.widget2)
        self.path_edit.setObjectName("path_edit")
        self.horizontalLayout_3.addWidget(self.path_edit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "百度图片", None, QtGui.QApplication.UnicodeUTF8))
        self.go.setText(QtGui.QApplication.translate("Form", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.get_path.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.key_label.setText(QtGui.QApplication.translate("Form", "关键字", None, QtGui.QApplication.UnicodeUTF8))
        self.page_label.setText(QtGui.QApplication.translate("Form", "页数", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "地址", None, QtGui.QApplication.UnicodeUTF8))

