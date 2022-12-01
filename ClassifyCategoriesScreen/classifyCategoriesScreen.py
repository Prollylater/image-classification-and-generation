#Classify and Generate Image Classify Categories screen

#APP Imports
import sys

from HomeScreen.homeScreen import HomeScreenWindow

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *

#pyside2-uic to change from ui to py
#pyrcc to change from qrc to py

#Import user interface file
from ClassifyCategoriesScreen import ui_classifyCategoriesScreen


#Main Class
class ClassifyCategoriesScreenWindow(QMainWindow):
    def __init__(self):
        ui_classifyCategoriesScreen.QMainWindow.__init__(self)
        self.ui = ui_classifyCategoriesScreen.Ui_ClassifyCategoriesWindow()
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
        self.shadow = ui_classifyCategoriesScreen.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(ui_classifyCategoriesScreen.QColor(0, 0, 0, 120))
        #Apply shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #Button click events
        #Minimize window
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        #Close Window
        self.ui.closeButton.clicked.connect(lambda: self.close())
        #Go Back Button
        self.ui.GoBack.clicked.connect(self.openHomeWindow)
        #Animals Button
        self.ui.AnimalsButton.clicked.connect(self.openAnimalsWindow)
        #Plants Button
        self.ui.PlantsButton.clicked.connect(self.openPlantsWindow)
        #Vehicles Button
        self.ui.VehicleButton.clicked.connect(self.openVehiclesWindow)
        #Logo Button
        self.ui.LogosButton.clicked.connect(self.openLogoWindow)
        #Clothes Button
        self.ui.ClothesButton.clicked.connect(self.openClothesWindow)
        #Music Instruments Button
        self.ui.MIButton.clicked.connect(self.openInstrumentsWindow)

        #Move window on mouse drag event on the title bar
        def moveWindow(e):
            #only accept when left button is clicked
            if e.buttons() == ui_classifyCategoriesScreen.Qt.LeftButton:
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

    # Open Home Window
    def openHomeWindow(self):
        self.window = HomeScreenWindow()
        ClassifyCategoriesScreenWindow.close(self)
        self.window.show()

    # Open Animals Window
    def openAnimalsWindow(self):
        from Classify.animalsScreen import AnimalsScreenWindow
        self.window = AnimalsScreenWindow()
        ClassifyCategoriesScreenWindow.close(self)
        self.window.show()

    def openPlantsWindow(self):
        from Classify.plantScreen import PlantScreenWindow
        self.window = PlantScreenWindow()
        ClassifyCategoriesScreenWindow.close(self)
        self.window.show()

    def openVehiclesWindow(self):
        from Classify.vehiclesScreen import VehiclesScreenWindow
        self.window = VehiclesScreenWindow()
        ClassifyCategoriesScreenWindow.close(self)
        self.window.show()

    def openLogoWindow(self):
        from Classify.logoScreen import LogoScreenWindow
        self.window = LogoScreenWindow()
        ClassifyCategoriesScreenWindow.close(self)
        self.window.show()

    def openClothesWindow(self):
        from Classify.clothesScreen import ClothesScreenWindow
        self.window = ClothesScreenWindow()
        ClassifyCategoriesScreenWindow.close(self)
        self.window.show()

    def openInstrumentsWindow(self):
        from Classify.instrumentsScreen import InstrumentsScreenWindow
        self.window = InstrumentsScreenWindow()
        ClassifyCategoriesScreenWindow.close(self)
        self.window.show()

    # Mouse events to the window
    def mousePressEvent(self, event):
        # get current position of the mouse
        self.clickPosition = event.globalPos()



#executable command
if __name__ == "__main__":
    app = ui_classifyCategoriesScreen.QApplication(sys.argv)
    window = ClassifyCategoriesScreenWindow()
    sys.exit(app.exec_())
