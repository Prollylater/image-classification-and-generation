#Classify and Generate Image Classify Main screen

#APP Imports
import sys

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PyQt5 import Qt
from Classify.ClassifyProgram.PredictionFunctions import PredictWithBaseModel

#pyside2-uic to change from ui to py
#pyrcc to change from qrc to py

#Import user interface file
from Generate import ui_generateScreen
progressBarValue = 0

#Main Class
class GenerateWindow(QMainWindow):
    def __init__(self):
        ui_generateScreen.QMainWindow.__init__(self)
        self.ui = ui_generateScreen.Ui_GenerateWindow()
        self.ui.setupUi(self)
        self.center()

        # Remove window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Set Window Icon
        self.setWindowIcon(QtGui.QIcon(":/Images/Images/logoDeskApp.png"))
        # Set Window title
        self.setWindowTitle("CGI App")

        #Font Downlaod
        QtGui.QFontDatabase.addApplicationFont("Resources/Futura Md BT.ttf")

        #Apply shadow effect
        self.shadow = ui_generateScreen.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(ui_generateScreen.QColor(0, 0, 0, 120))
        #Apply shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #Button click events
        #Minimize window
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        #Close Window
        self.ui.closeButton.clicked.connect(lambda: self.close())
        #Go Back Button
        self.ui.GoBack.clicked.connect(self.openHomeWindow)
        #Generate Button
        self.ui.generateButton.clicked.connect(self.generateButton)

        #Download Button
        #self.ui.downloadButton.clicked.connect(self.connectButton)


        #Move window on mouse drag event on the title bar
        def moveWindow(e):
            #only accept when left button is clicked
            if e.buttons() == ui_generateScreen.Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

        #Add click event/mouse move event /drag event to the top header to move the window
        self.ui.main_header.mouseMoveEvent = moveWindow



        #Show window
        self.show()


    #Center the Window
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


    def openHomeWindow(self):
        from HomeScreen.homeScreen import HomeScreenWindow
        self.window = HomeScreenWindow()
        GenerateWindow.close(self)
        self.window.show()

    # Mouse events to the window
    def mousePressEvent(self, event):
        # get current position of the mouse
        self.clickPosition = event.globalPos()

    def generateProgress(self):
        global progressBarValue

        #apply progressbarvalue to proress bar
        self.ui.progressBar.setValue(progressBarValue)

        #view progress bar value and update status text and close screen and open home window
        if progressBarValue > 100:
            #reset timer
            self.timer.stop()
            progressBarValue = 0
            #change the Status text
            from _ast import Lambda
            QtCore.QTimer.singleShot(0,lambda :self.ui.loadingStatus.setText("Loading completed"))

        elif progressBarValue < 2:
            QtCore.QTimer.singleShot(0, lambda: self.ui.generatingLabel.setText("Generating Image"))

        elif progressBarValue < 20:
            QtCore.QTimer.singleShot(0, lambda: self.ui.loadingStatus.setText("Please Wait"))

        elif progressBarValue < 40:
            QtCore.QTimer.singleShot(0, lambda: self.ui.loadingStatus.setText("Collecting Data"))

        elif progressBarValue < 60:
            QtCore.QTimer.singleShot(0, lambda: self.ui.loadingStatus.setText("Painting Image"))

        elif progressBarValue < 80:
            QtCore.QTimer.singleShot(0, lambda: self.ui.loadingStatus.setText("Analyzing"))

        elif progressBarValue < 100:
            QtCore.QTimer.singleShot(0, lambda: self.ui.loadingStatus.setText("Loading results"))


        #increase progressBarValue by 1 after time interval in millisecond;
        progressBarValue +=1


    def openTimer(self):
        self.timer = QtCore.QTimer()
        # Time intervall in milliseconds
        self.timer.start(30)
        progressBarValue = 0
        self.ui.progressBar.setValue(progressBarValue)
        self.timer.timeout.connect(self.generateProgress)

    def resetTimerAndGenerateImage(self):
        #Reset Timer
        progressBarValue = 0
        # apply progressbarvalue to proress bar
        self.ui.progressBar.setValue(progressBarValue)
        QtCore.QTimer.singleShot(0, lambda: self.ui.generatingLabel.setText(""))
        QtCore.QTimer.singleShot(0, lambda: self.ui.loadingStatus.setText(""))


    def generateButton(self):
        self.openTimer()
        self.resetTimerAndGenerateImage()


#executable command
if __name__ == "__main__":
    app = ui_generateScreen.QApplication(sys.argv)
    window = GenerateWindow()
    sys.exit(app.exec_())
