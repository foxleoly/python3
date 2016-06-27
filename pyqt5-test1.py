# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt5-test1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.btn = QtWidgets.QDialogButtonBox(Dialog)
        self.btn.setGeometry(QtCore.QRect(50, 260, 341, 32))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setItalic(False)
        self.btn.setFont(font)
        self.btn.setOrientation(QtCore.Qt.Horizontal)
        self.btn.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.btn.setObjectName("btn")
        self.table1 = QtWidgets.QTableView(Dialog)
        self.table1.setGeometry(QtCore.QRect(10, 10, 381, 231))
        self.table1.setObjectName("table1")

        self.retranslateUi(Dialog)
        self.btn.accepted.connect(Dialog.accept)
        self.btn.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
