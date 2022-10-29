# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadingScreen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from LoadingScreen import splash_screen_rc

class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        if not MainScreen.objectName():
            MainScreen.setObjectName(u"MainScreen")
        MainScreen.resize(800, 600)
        self.centralwidget = QWidget(MainScreen)
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
        self.robot.setStyleSheet(u"image: url(:/Images/Images/Banner.png);")
        self.robot.setFrameShape(QFrame.StyledPanel)
        self.robot.setFrameShadow(QFrame.Raised)
        self.logo = QFrame(self.mainFrame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, 20, 241, 91))
        self.logo.setStyleSheet(u"image: url(:/Images/Images/logoApp.png);\n"
"background-color:transparent;")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.description = QFrame(self.mainFrame)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(0, 140, 301, 161))
        self.description.setStyleSheet(u"image: url(:/Images/Images/descApp.png);")
        self.description.setFrameShape(QFrame.StyledPanel)
        self.description.setFrameShadow(QFrame.Raised)
        self.initializing = QLabel(self.mainFrame)
        self.initializing.setObjectName(u"initializing")
        self.initializing.setGeometry(QRect(50, 410, 201, 21))
        font = QFont()
        font.setFamily(u"Futura Md BT")
        font.setPointSize(10)
        self.initializing.setFont(font)
        self.initializing.setStyleSheet(u"background-color:transparent;\n"
"border: none;")
        self.initializing.setAlignment(Qt.AlignCenter)
        self.loadingStatus = QLabel(self.mainFrame)
        self.loadingStatus.setObjectName(u"loadingStatus")
        self.loadingStatus.setGeometry(QRect(160, 460, 201, 21))
        font1 = QFont()
        font1.setFamily(u"Futura Md BT")
        font1.setPointSize(7)
        self.loadingStatus.setFont(font1)
        self.loadingStatus.setStyleSheet(u"background-color:transparent;\n"
"border: none;")
        self.loadingStatus.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.mainFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 433, 231, 21))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color:transparent;\n"
"	color:transparent;\n"
"	text-align:left;\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color:#f16150;\n"
"	border-radius:10px;\n"
"}")
        self.progressBar.setValue(24)
        MainScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainScreen)

        QMetaObject.connectSlotsByName(MainScreen)
    # setupUi

    def retranslateUi(self, MainScreen):
        MainScreen.setWindowTitle(QCoreApplication.translate("MainScreen", u"MainWindow", None))
        self.initializing.setText(QCoreApplication.translate("MainScreen", u"Initializing App", None))
        self.loadingStatus.setText(QCoreApplication.translate("MainScreen", u"Please Wait ...", None))
    # retranslateUi

