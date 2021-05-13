# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(60, 280, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        # self.label_3.setFont(font)
        # self.label_3.setStyleSheet("color: rgb(0, 117, 210);")
        # self.label_3.setWordWrap(True)
        # self.label_3.setObjectName("label_3")
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(60, 250, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        # self.label_2.setFont(font)
        # self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        # self.label_2.setWordWrap(True)
        # self.label_2.setObjectName("label_2")
        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(-10, 0, 543, 300))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/13.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")

        self.voiceFig_2 = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig_2.setGeometry(QtCore.QRect(190, 410, 121, 133))
        self.voiceFig_2.setText("")
        self.gif_2 = QMovie("icon/play.gif")
        self.voiceFig_2.setMovie(self.gif_2)
        self.gif_2.start()
        self.voiceFig_2.setScaledContents(True)
        self.voiceFig_2.setObjectName("voiceFig_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 360, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label")
        self.label_2.setVisible(False)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 360, 400, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label.setVisible(True)
        # self.label_4 = QtWidgets.QLabel(self.centralwidget)
        # self.label_4.setGeometry(QtCore.QRect(60, 330, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        # self.label_4.setFont(font)
        # self.label_4.setStyleSheet("color: rgb(0, 117, 210);")
        # self.label_4.setWordWrap(True)
        # self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        # self.label_3.setText(_translate("MainWindow", "1. Enjoy music by saying \"Play music\""))
        # self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label.setText(_translate("MainWindow", "I'm asleep! Wake me up by saying 'hey'!"))
        self.label_2.setText(_translate("MainWindow", "Hi! How can I help?"))
        # self.label_4.setText(_translate("MainWindow", "2. Take some notes by saying \"Open Notepad\""))

