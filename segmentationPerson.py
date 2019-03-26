# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'segmentationPerson.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(736, 614)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.originImg = QtWidgets.QGraphicsView(self.splitter)
        self.originImg.setObjectName("originImg")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.choosePic = QtWidgets.QPushButton(self.frame)
        self.choosePic.setObjectName("choosePic")
        self.verticalLayout.addWidget(self.choosePic)
        self.segPic = QtWidgets.QPushButton(self.frame)
        self.segPic.setObjectName("segPic")
        self.verticalLayout.addWidget(self.segPic)
        self.segImg = QtWidgets.QGraphicsView(self.splitter)
        self.segImg.setObjectName("segImg")
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.choosePic.setText(_translate("Dialog", "Choose Picture"))
        self.segPic.setText(_translate("Dialog", "Segmentation"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Ui_Dialog()
    w.show()
    sys.exit(app.exec_())