#Classify and Generate Image Loading screen

#APP Imports
import sys
import os
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#Import user interface file
from ui_splashScreen import *

#Main Class
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Remove window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        #Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,120))
        #Apply shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #Show window
        self.show()

#executable command
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
