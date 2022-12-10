# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generateScreen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from HomeScreen import home_screen_rc

class Ui_GenerateWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1130, 779)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.MainFrame = QFrame(self.centralwidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setGeometry(QRect(10, 10, 1107, 756))
        self.MainFrame.setStyleSheet(u"background-color: #2b3e47;\n"
"border-radius: 25px;")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.circle1 = QFrame(self.MainFrame)
        self.circle1.setObjectName(u"circle1")
        self.circle1.setGeometry(QRect(-90, 330, 351, 261))
        self.circle1.setStyleSheet(u"image: url(:/Images/Images/circle1.png);")
        self.circle1.setFrameShape(QFrame.StyledPanel)
        self.circle1.setFrameShadow(QFrame.Raised)
        self.logo = QFrame(self.MainFrame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(20, 10, 141, 51))
        self.logo.setStyleSheet(u"image: url(:/Images/Images/logoAppWhite.png);")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.circle2 = QFrame(self.MainFrame)
        self.circle2.setObjectName(u"circle2")
        self.circle2.setGeometry(QRect(730, 30, 631, 761))
        self.circle2.setStyleSheet(u"image: url(:/Images/Images/circle1.png);\n"
"background-color: transparent;")
        self.circle2.setFrameShape(QFrame.StyledPanel)
        self.circle2.setFrameShadow(QFrame.Raised)
        self.GoBack = QPushButton(self.circle2)
        self.GoBack.setObjectName(u"GoBack")
        self.GoBack.setGeometry(QRect(254, 670, 121, 51))
        self.GoBack.setCursor(QCursor(Qt.PointingHandCursor))
        self.GoBack.setStyleSheet(u"background-color:transparent;\n"
"image:none;\n"
"color: #fff;\n"
"font: 11pt \"Futura Md BT\";\n"
"")
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

        self.main_header = QFrame(self.MainFrame)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setGeometry(QRect(0, 0, 1111, 131))
        self.main_header.setStyleSheet(u"background-color:transparent;")
        self.main_header.setFrameShape(QFrame.StyledPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.robot = QFrame(self.MainFrame)
        self.robot.setObjectName(u"robot")
        self.robot.setGeometry(QRect(10, 680, 61, 71))
        self.robot.setStyleSheet(u"image: url(:/Images/Images/robot.png);\n"
"background-color:transparent;")
        self.robot.setFrameShape(QFrame.StyledPanel)
        self.robot.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.MainFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(620, 130, 371, 361))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: rgb(12, 22, 33);\n"
"border-radius : 20px;")
        self.label.setPixmap(QPixmap(u":/Images/Images/robot.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.generatingLabel = QLabel(self.MainFrame)
        self.generatingLabel.setObjectName(u"generatingLabel")
        self.generatingLabel.setGeometry(QRect(140, 510, 201, 21))
        font = QFont()
        font.setFamily(u"Futura Md BT")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(1)
        self.generatingLabel.setFont(font)
        self.generatingLabel.setStyleSheet(u"background-color:transparent;\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"font: 10 pt \"Futura Md BT\";")
        self.generatingLabel.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.MainFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(130, 550, 231, 21))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color:transparent;\n"
"	color:transparent;\n"
"	text-align:left;\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color:#f16150;\n"
"	border-radius:10px;\n"
"}")
        self.progressBar.setValue(0)
        self.loadingStatus = QLabel(self.MainFrame)
        self.loadingStatus.setObjectName(u"loadingStatus")
        self.loadingStatus.setGeometry(QRect(250, 577, 201, 21))
        font1 = QFont()
        font1.setFamily(u"Futura Md BT")
        font1.setPointSize(7)
        self.loadingStatus.setFont(font1)
        self.loadingStatus.setStyleSheet(u"background-color:transparent;\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.loadingStatus.setAlignment(Qt.AlignCenter)
        self.generateButton = QPushButton(self.MainFrame)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setGeometry(QRect(170, 437, 141, 41))
        font2 = QFont()
        font2.setFamily(u"Futura Md BT")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.generateButton.setFont(font2)
        self.generateButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.generateButton.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #2b3e47, stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	font: 11pt \"Futura Md BT\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgb(63, 102, 120), stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	font: 13pt \"Futura Md BT\";\n"
"}\n"
"")
        self.downloadButton = QPushButton(self.MainFrame)
        self.downloadButton.setObjectName(u"downloadButton")
        self.downloadButton.setGeometry(QRect(720, 530, 171, 41))
        self.downloadButton.setFont(font2)
        self.downloadButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.downloadButton.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #2b3e47, stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	font: 11pt \"Futura Md BT\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgb(63, 102, 120), stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	font: 13pt \"Futura Md BT\";\n"
"}\n"
"")
        self.generateInput = QLineEdit(self.MainFrame)
        self.generateInput.setObjectName(u"generateInput")
        self.generateInput.setGeometry(QRect(60, 360, 361, 41))
        self.generateInput.setStyleSheet(u"background-color: rgba(234, 239, 244, 247);\n"
"border : solid 2px rgb(34, 46, 59);\n"
"border-radius : 20px;\n"
"padding-left : 15px;")
        self.generateInput.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.questionText1 = QLabel(self.MainFrame)
        self.questionText1.setObjectName(u"questionText1")
        self.questionText1.setGeometry(QRect(190, 240, 111, 51))
        self.questionText1.setLayoutDirection(Qt.LeftToRight)
        self.questionText1.setStyleSheet(u"background-color: rgba(212, 221, 232, 0);\n"
"color: rgb(243, 243, 243);\n"
"font: 11pt \"Futura Md BT\";\n"
"text-align : center;")
        self.questionText1.setAlignment(Qt.AlignCenter)
        self.questionText1_2 = QLabel(self.MainFrame)
        self.questionText1_2.setObjectName(u"questionText1_2")
        self.questionText1_2.setGeometry(QRect(90, 270, 301, 51))
        self.questionText1_2.setLayoutDirection(Qt.LeftToRight)
        self.questionText1_2.setStyleSheet(u"background-color: rgba(212, 221, 232, 0);\n"
"color: rgb(243, 243, 243);\n"
"font: 11pt \"Futura Md BT\";\n"
"text-align : center;")
        self.questionText1_2.setAlignment(Qt.AlignCenter)
        self.logo.raise_()
        self.circle1.raise_()
        self.circle2.raise_()
        self.circle3.raise_()
        self.circle4.raise_()
        self.main_header.raise_()
        self.windowNav.raise_()
        self.robot.raise_()
        self.label.raise_()
        self.generatingLabel.raise_()
        self.progressBar.raise_()
        self.loadingStatus.raise_()
        self.generateButton.raise_()
        self.downloadButton.raise_()
        self.generateInput.raise_()
        self.questionText1.raise_()
        self.questionText1_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.GoBack.setText(QCoreApplication.translate("MainWindow", u"Go Back", None))
        self.minimizeButton.setText("")
        self.closeButton.setText("")
        self.label.setText("")
        self.generatingLabel.setText("")
        self.loadingStatus.setText("")
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.downloadButton.setText(QCoreApplication.translate("MainWindow", u"Download Image", None))
        self.generateInput.setText("")
        self.generateInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Express your imagination here !", None))
        self.questionText1.setText(QCoreApplication.translate("MainWindow", u"Hello Human !", None))
        self.questionText1_2.setText(QCoreApplication.translate("MainWindow", u"Tell me what do you want to generate ?", None))
    # retranslateUi

