# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'classifyCategoriesScreen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from HomeScreen import home_screen_rc

class Ui_ClassifyCategoriesWindow(object):
    def setupUi(self, ClassifyCategoriesWindow):
        if not ClassifyCategoriesWindow.objectName():
            ClassifyCategoriesWindow.setObjectName(u"ClassifyCategoriesWindow")
        ClassifyCategoriesWindow.resize(1126, 784)
        self.centralwidget = QWidget(ClassifyCategoriesWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.MainFrame = QFrame(self.centralwidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setGeometry(QRect(10, 10, 1107, 756))
        self.MainFrame.setStyleSheet(u"background-color: #2b3e47;\n"
"border-radius: 25px;")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.AnimalsButton = QPushButton(self.MainFrame)
        self.AnimalsButton.setObjectName(u"AnimalsButton")
        self.AnimalsButton.setGeometry(QRect(180, 110, 221, 161))
        font = QFont()
        font.setPointSize(17)
        self.AnimalsButton.setFont(font)
        self.AnimalsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.AnimalsButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.AnimalsButton.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #2b3e47, stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgb(63, 102, 120), stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	font-size : 25px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/Images/Images/Classify Icons/Animals.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AnimalsButton.setIcon(icon)
        self.AnimalsButton.setIconSize(QSize(150, 150))
        self.AnimalsButton.setAutoDefault(False)
        self.circle1 = QFrame(self.MainFrame)
        self.circle1.setObjectName(u"circle1")
        self.circle1.setGeometry(QRect(20, 430, 351, 261))
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
        icon1 = QIcon()
        icon1.addFile(u":/Images/Images/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon1)
        self.minimizeButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.minimizeButton)

        self.closeButton = QPushButton(self.windowNav)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMaximumSize(QSize(50, 50))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Images/Images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)
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
        self.PlantsButton = QPushButton(self.MainFrame)
        self.PlantsButton.setObjectName(u"PlantsButton")
        self.PlantsButton.setGeometry(QRect(440, 110, 221, 161))
        self.PlantsButton.setFont(font)
        self.PlantsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.PlantsButton.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #2b3e47, stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgb(63, 102, 120), stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	font-size : 25px;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/Images/Images/Classify Icons/Plants.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PlantsButton.setIcon(icon3)
        self.PlantsButton.setIconSize(QSize(150, 150))
        self.VehicleButton = QPushButton(self.MainFrame)
        self.VehicleButton.setObjectName(u"VehicleButton")
        self.VehicleButton.setGeometry(QRect(700, 110, 221, 161))
        self.VehicleButton.setFont(font)
        self.VehicleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.VehicleButton.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #2b3e47, stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgb(63, 102, 120), stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	font-size : 25px;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/Images/Images/Classify Icons/vehicles.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VehicleButton.setIcon(icon4)
        self.VehicleButton.setIconSize(QSize(150, 150))
        self.LogosButton = QPushButton(self.MainFrame)
        self.LogosButton.setObjectName(u"LogosButton")
        self.LogosButton.setGeometry(QRect(700, 310, 221, 161))
        self.LogosButton.setFont(font)
        self.LogosButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.LogosButton.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #2b3e47, stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgb(63, 102, 120), stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	font-size : 25px;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/Images/Images/Classify Icons/Logos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.LogosButton.setIcon(icon5)
        self.LogosButton.setIconSize(QSize(150, 150))
        self.ArtistsButton = QPushButton(self.MainFrame)
        self.ArtistsButton.setObjectName(u"ArtistsButton")
        self.ArtistsButton.setGeometry(QRect(180, 310, 221, 161))
        self.ArtistsButton.setFont(font)
        self.ArtistsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ArtistsButton.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #2b3e47, stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgb(63, 102, 120), stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	font-size : 25px;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/Images/Images/Classify Icons/Artists.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ArtistsButton.setIcon(icon6)
        self.ArtistsButton.setIconSize(QSize(150, 150))
        self.AthletesButton = QPushButton(self.MainFrame)
        self.AthletesButton.setObjectName(u"AthletesButton")
        self.AthletesButton.setGeometry(QRect(440, 310, 221, 161))
        self.AthletesButton.setFont(font)
        self.AthletesButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.AthletesButton.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #2b3e47, stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgb(63, 102, 120), stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	font-size : 25px;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/Images/Images/Classify Icons/Athletes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AthletesButton.setIcon(icon7)
        self.AthletesButton.setIconSize(QSize(150, 150))
        self.MIButton = QPushButton(self.MainFrame)
        self.MIButton.setObjectName(u"MIButton")
        self.MIButton.setGeometry(QRect(180, 510, 221, 161))
        self.MIButton.setFont(font)
        self.MIButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.MIButton.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #2b3e47, stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgb(63, 102, 120), stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	font-size : 25px;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/Images/Images/Classify Icons/MusicInstruments.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MIButton.setIcon(icon8)
        self.MIButton.setIconSize(QSize(150, 150))
        self.DishesButton = QPushButton(self.MainFrame)
        self.DishesButton.setObjectName(u"DishesButton")
        self.DishesButton.setGeometry(QRect(700, 510, 221, 161))
        self.DishesButton.setFont(font)
        self.DishesButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.DishesButton.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #2b3e47, stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgb(63, 102, 120), stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	font-size : 25px;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/Images/Images/Classify Icons/Dishes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DishesButton.setIcon(icon9)
        self.DishesButton.setIconSize(QSize(150, 150))
        self.ClothesButton = QPushButton(self.MainFrame)
        self.ClothesButton.setObjectName(u"ClothesButton")
        self.ClothesButton.setGeometry(QRect(440, 510, 221, 161))
        self.ClothesButton.setFont(font)
        self.ClothesButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ClothesButton.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #2b3e47, stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgb(63, 102, 120), stop:1 #f16150);\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	font-size : 25px;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/Images/Images/Classify Icons/Clothes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ClothesButton.setIcon(icon10)
        self.ClothesButton.setIconSize(QSize(150, 150))
        self.logo.raise_()
        self.circle1.raise_()
        self.circle2.raise_()
        self.circle3.raise_()
        self.AnimalsButton.raise_()
        self.circle4.raise_()
        self.main_header.raise_()
        self.windowNav.raise_()
        self.robot.raise_()
        self.PlantsButton.raise_()
        self.VehicleButton.raise_()
        self.LogosButton.raise_()
        self.ArtistsButton.raise_()
        self.AthletesButton.raise_()
        self.MIButton.raise_()
        self.DishesButton.raise_()
        self.ClothesButton.raise_()
        ClassifyCategoriesWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ClassifyCategoriesWindow)

        QMetaObject.connectSlotsByName(ClassifyCategoriesWindow)
    # setupUi

    def retranslateUi(self, ClassifyCategoriesWindow):
        ClassifyCategoriesWindow.setWindowTitle(QCoreApplication.translate("ClassifyCategoriesWindow", u"MainWindow", None))
        self.AnimalsButton.setText("")
        self.GoBack.setText(QCoreApplication.translate("ClassifyCategoriesWindow", u"Go Back", None))
        self.minimizeButton.setText("")
        self.closeButton.setText("")
        self.PlantsButton.setText("")
        self.VehicleButton.setText("")
        self.LogosButton.setText("")
        self.ArtistsButton.setText("")
        self.AthletesButton.setText("")
        self.MIButton.setText("")
        self.DishesButton.setText("")
        self.ClothesButton.setText("")
    # retranslateUi

