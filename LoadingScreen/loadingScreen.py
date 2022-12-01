#Classify and Generate Image Loading screen

#APP Imports
import sys

from PySide2.QtGui import QColor
from PySide2.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QApplication

from HomeScreen.homeScreen import HomeScreenWindow

from PySide2 import QtCore, QtGui, QtWidgets

#pyside2-uic to change from ui to py
#pyrcc to change from qrc to py

#Import user interface file
from LoadingScreen import ui_loadingScreen
progressBarValue = 0


#Loading Screen Class
class LoadingScreenWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_loadingScreen.Ui_MainScreen()
        self.ui.setupUi(self)
        #center the window
        self.center()
        #Set Window Icon
        self.setWindowIcon(QtGui.QIcon("Images/logoDeskApp.png"))
        #Set Window title
        self.setWindowTitle("CGI App")
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

        #use QTIMER to delay the progressBar

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.appProgress)
        #Time intervall in milliseconds
        self.timer.start(50)

        #Show window
        self.show()



    #Function to center the Main Widget
    def center(self):
        # center window
        window = self.window()
        window.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignCenter,
                window.size(),
                QtGui.QGuiApplication.primaryScreen().availableGeometry(),
            ),
        )


    #Define appProgress functiion
    def appProgress(self):
            global progressBarValue
            #apply progressbarvalue to proress bar
            self.ui.progressBar.setValue(progressBarValue)

            #view progress bar value and update status text and close screen and open home window
            if progressBarValue > 100:
                #reset timer
                self.timer.stop()

                #Open Home Screen Window after progress bar finnished
                self.main = HomeScreenWindow()
                self.main.show()

                #close the splash screen
                self.close()

                #change the loadingStatus text
                from _ast import Lambda
                QtCore.QTimer.singleShot(0,lambda :self.ui.loadingStatus.setText("Loading completed"))

            elif progressBarValue < 20:
                QtCore.QTimer.singleShot(0, lambda: self.ui.loadingStatus.setText("Please Wait"))

            elif progressBarValue < 40:
                QtCore.QTimer.singleShot(0, lambda: self.ui.loadingStatus.setText("Generating App"))

            elif progressBarValue < 60:
                QtCore.QTimer.singleShot(0, lambda: self.ui.loadingStatus.setText("Initializing A.I"))

            elif progressBarValue < 80:
                QtCore.QTimer.singleShot(0, lambda: self.ui.loadingStatus.setText("Collecting Data"))

            elif progressBarValue < 100:
                QtCore.QTimer.singleShot(0, lambda: self.ui.loadingStatus.setText("Loading content"))

            #increase progressBarValue by 1 after time interval in millisecond;
            progressBarValue +=1

#executable command
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadingScreenWindow()
    sys.exit(app.exec_())
