# -*- coding: utf-8 -*-
import os

################################################################################
## Form generated from reading UI file 'splashScreenvCjTMK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#os.system('Pyrcc5 splash_screen.qrc -o splash_screen_rc.py')


import splash_screen_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(50, 40, 691, 491))
        self.mainFrame.setStyleSheet(u"background-color: #fff;\n"
                                     "border-radius: 20px;\n"
                                     "")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.robot = QFrame(self.mainFrame)
        self.robot.setObjectName(u"robot")
        self.robot.setGeometry(QRect(290, 20, 391, 451))
        self.robot.setStyleSheet(u"image: url(:/images/Images/robot.png);\n"
                                 "image: url(:/images/Images/Banner.png);")
        self.robot.setFrameShape(QFrame.StyledPanel)
        self.robot.setFrameShadow(QFrame.Raised)
        self.logo = QFrame(self.mainFrame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(20, 20, 171, 71))
        self.logo.setStyleSheet(u"image: url(:/images/Images/logoApp.png);")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.description = QFrame(self.mainFrame)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(0, 140, 301, 161))
        self.description.setStyleSheet(u"image: url(:/images/Images/descApp.png);")
        self.description.setFrameShape(QFrame.StyledPanel)
        self.description.setFrameShadow(QFrame.Raised)
        self.initializing = QLabel(self.mainFrame)
        self.initializing.setObjectName(u"initializing")
        self.initializing.setGeometry(QRect(40, 410, 201, 21))
        font = QFont()
        font.setFamily(u"Futura Md BT")
        font.setPointSize(10)
        self.initializing.setFont(font)
        self.initializing.setStyleSheet(u"background-color:transparent;\n"
                                        "border: none;")
        self.initializing.setAlignment(Qt.AlignCenter)
        self.loading_press = QLabel(self.mainFrame)
        self.loading_press.setObjectName(u"loading_press")
        self.loading_press.setGeometry(QRect(160, 460, 201, 21))
        font1 = QFont()
        font1.setFamily(u"Futura Md BT")
        font1.setPointSize(7)
        self.loading_press.setFont(font1)
        self.loading_press.setStyleSheet(u"background-color:transparent;\n"
                                         "border: none;")
        self.loading_press.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.initializing.setText(QCoreApplication.translate("MainWindow", u"Initializing App", None))
        self.loading_press.setText(QCoreApplication.translate("MainWindow", u"Please Wait ...", None))
    # retranslateUi
