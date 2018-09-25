# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'organizeFileUi.ui'
#
# Created: Mon Sep 17 21:34:45 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(393, 104)
        font = QtGui.QFont()
        Form.setFont(font)
        Form.setCursor(QtCore.Qt.ArrowCursor)
        Form.setAutoFillBackground(False)
        self.path_edit = QtGui.QLineEdit(Form)
        self.path_edit.setGeometry(QtCore.QRect(40, 10, 311, 20))
        self.path_edit.setObjectName("path_edit")
        self.path_label = QtGui.QLabel(Form)
        self.path_label.setGeometry(QtCore.QRect(10, 10, 31, 21))
        self.path_label.setObjectName("path_label")
        self.set_path = QtGui.QPushButton(Form)
        self.set_path.setGeometry(QtCore.QRect(360, 10, 31, 21))
        self.set_path.setObjectName("set_path")
        self.time_label = QtGui.QLabel(Form)
        self.time_label.setGeometry(QtCore.QRect(10, 40, 31, 21))
        self.time_label.setObjectName("time_label")
        self.dateEdit = QtGui.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(40, 40, 110, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 9, 17), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setObjectName("dateEdit")
        self.complete_info = QtGui.QLabel(Form)
        self.complete_info.setEnabled(False)
        self.complete_info.setGeometry(QtCore.QRect(160, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.complete_info.setFont(font)
        self.complete_info.setMouseTracking(True)
        self.complete_info.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.complete_info.setStatusTip("")
        self.complete_info.setAutoFillBackground(False)
        self.complete_info.setInputMethodHints(QtCore.Qt.ImhNone)
        self.complete_info.setText("")
        self.complete_info.setTextFormat(QtCore.Qt.AutoText)
        self.complete_info.setObjectName("complete_info")
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(40, 70, 341, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.Go = QtGui.QPushButton(Form)
        self.Go.setGeometry(QtCore.QRect(280, 40, 71, 23))
        self.Go.setObjectName("Go")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "文件整理", None, QtGui.QApplication.UnicodeUTF8))
        self.path_edit.setToolTip(QtGui.QApplication.translate("Form", "设置需要整理的路径", None, QtGui.QApplication.UnicodeUTF8))
        self.path_label.setText(QtGui.QApplication.translate("Form", "路径：", None, QtGui.QApplication.UnicodeUTF8))
        self.set_path.setToolTip(QtGui.QApplication.translate("Form", "点击获取路径", None, QtGui.QApplication.UnicodeUTF8))
        self.set_path.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.time_label.setText(QtGui.QApplication.translate("Form", "时间：", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEdit.setToolTip(QtGui.QApplication.translate("Form", "设置判断文件的时间周期", None, QtGui.QApplication.UnicodeUTF8))
        self.Go.setText(QtGui.QApplication.translate("Form", "开始整理", None, QtGui.QApplication.UnicodeUTF8))

