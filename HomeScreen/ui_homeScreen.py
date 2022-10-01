# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeScreen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import home_screen_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1125, 774)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.MainFrame = QFrame(self.centralwidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setStyleSheet(u"background-color: #2b3e47;\n"
"border-radius: 25px;")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.classifyButton = QPushButton(self.MainFrame)
        self.classifyButton.setObjectName(u"classifyButton")
        self.classifyButton.setGeometry(QRect(270, 490, 221, 51))
        font = QFont()
        font.setPointSize(17)
        self.classifyButton.setFont(font)
        self.classifyButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.classifyButton.setStyleSheet(u"QPushButton{\n"
"	background-color:#f16150;\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(185, 74, 61);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	font-size : 20px;\n"
"}\n"
"")
        self.circle1 = QFrame(self.MainFrame)
        self.circle1.setObjectName(u"circle1")
        self.circle1.setGeometry(QRect(20, 430, 351, 261))
        self.circle1.setStyleSheet(u"image: url(:/Images/Images/circle1.png);")
        self.circle1.setFrameShape(QFrame.StyledPanel)
        self.circle1.setFrameShadow(QFrame.Raised)
        self.logo = QFrame(self.MainFrame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(20, 10, 261, 141))
        self.logo.setStyleSheet(u"image: url(:/Images/Images/logoAppWhite.png);")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.circle2 = QFrame(self.MainFrame)
        self.circle2.setObjectName(u"circle2")
        self.circle2.setGeometry(QRect(630, 60, 631, 661))
        self.circle2.setStyleSheet(u"image: url(:/Images/Images/circle1.png);")
        self.circle2.setFrameShape(QFrame.StyledPanel)
        self.circle2.setFrameShadow(QFrame.Raised)
        self.robot = QFrame(self.circle2)
        self.robot.setObjectName(u"robot")
        self.robot.setGeometry(QRect(-80, 10, 341, 291))
        self.robot.setStyleSheet(u"image: url(:/Images/Images/robot.png);\n"
"background-color:transparent;")
        self.robot.setFrameShape(QFrame.StyledPanel)
        self.robot.setFrameShadow(QFrame.Raised)
        self.circle3 = QFrame(self.MainFrame)
        self.circle3.setObjectName(u"circle3")
        self.circle3.setGeometry(QRect(310, 190, 211, 171))
        self.circle3.setStyleSheet(u"image: url(:/Images/Images/circle2.png);\n"
"background-color:transparent;")
        self.circle3.setFrameShape(QFrame.StyledPanel)
        self.circle3.setFrameShadow(QFrame.Raised)
        self.circle4 = QFrame(self.MainFrame)
        self.circle4.setObjectName(u"circle4")
        self.circle4.setGeometry(QRect(490, 360, 101, 61))
        self.circle4.setStyleSheet(u"image: url(:/Images/Images/circle2.png);\n"
"background-color:transparent;")
        self.circle4.setFrameShape(QFrame.StyledPanel)
        self.circle4.setFrameShadow(QFrame.Raised)
        self.generateButton = QPushButton(self.MainFrame)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setGeometry(QRect(610, 490, 221, 51))
        self.generateButton.setFont(font)
        self.generateButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.generateButton.setLayoutDirection(Qt.LeftToRight)
        self.generateButton.setStyleSheet(u"QPushButton{\n"
"	background-color:#f16150;\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(185, 74, 61);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	font-size : 20px;\n"
"}")
        self.windowNav = QFrame(self.MainFrame)
        self.windowNav.setObjectName(u"windowNav")
        self.windowNav.setGeometry(QRect(1000, 10, 100, 40))
        self.windowNav.setMaximumSize(QSize(100, 40))
        self.windowNav.setStyleSheet(u"background-color:transparent;")
        self.windowNav.setFrameShape(QFrame.WinPanel)
        self.windowNav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.windowNav)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.windowNav)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMaximumSize(QSize(30, 30))
        self.minimizeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Images/Images/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon)
        self.minimizeButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.minimizeButton)

        self.closeButton = QPushButton(self.windowNav)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMaximumSize(QSize(50, 50))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Images/Images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon1)
        self.closeButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.closeButton)

        self.logo.raise_()
        self.circle1.raise_()
        self.circle2.raise_()
        self.circle3.raise_()
        self.classifyButton.raise_()
        self.circle4.raise_()
        self.generateButton.raise_()
        self.windowNav.raise_()

        self.horizontalLayout.addWidget(self.MainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.classifyButton.setText(QCoreApplication.translate("MainWindow", u"Classify", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.minimizeButton.setText("")
        self.closeButton.setText("")
    # retranslateUi

