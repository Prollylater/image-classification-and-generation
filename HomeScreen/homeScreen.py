#Classify and Generate Image Home screen

#APP Imports
import sys


from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *

#pyside2-uic to change from ui to py
#pyrcc to change from qrc to py

#Import user interface file
from HomeScreen import ui_homeScreen


#Main Class
class HomeScreenWindow(QMainWindow):
    def __init__(self):
        ui_homeScreen.QMainWindow.__init__(self)
        self.ui = ui_homeScreen.Ui_MainWindow()
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

        #Apply shadow effect
        self.shadow = ui_homeScreen.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(ui_homeScreen.QColor(0, 0, 0, 120))
        #Apply shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #Button click events
        #Minimize window
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        #Close Window
        self.ui.closeButton.clicked.connect(lambda: self.close())
        #Classify Button
        self.ui.classifyButton.clicked.connect(self.openClassifyWindow)
        #Generate Button
        self.ui.generateButton.clicked.connect(self.openGenerateWindow)

        #Move window on mouse drag event on the title bar
        def moveWindow(e):
            #only accept when left button is clicked
            if e.buttons() == ui_homeScreen.Qt.LeftButton:
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

    #Open Classify Window
    def openClassifyWindow(self):
        from ClassifyCategoriesScreen.classifyCategoriesScreen import ClassifyCategoriesScreenWindow
        self.window = ClassifyCategoriesScreenWindow()
        HomeScreenWindow.close(self)
        self.window.show()

    # Open Generate Window
    def openGenerateWindow(self):
        from Generate.generateScreen import GenerateWindow
        self.window = GenerateWindow()
        HomeScreenWindow.close(self)
        self.window.show()

    # Mouse events to the window
    def mousePressEvent(self, event):
        # get current position of the mouse
        self.clickPosition = event.globalPos()



#executable command
if __name__ == "__main__":
    app = ui_homeScreen.QApplication(sys.argv)
    window = HomeScreenWindow()
    sys.exit(app.exec_())
