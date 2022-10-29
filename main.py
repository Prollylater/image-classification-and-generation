import sys

from PySide2.QtWidgets import QApplication
from LoadingScreen.loadingScreen import LoadingScreenWindow

#executable command
if __name__ == "__main__":
    #Load first Screen : Loading Screen
    app = QApplication(sys.argv)
    window = LoadingScreenWindow()
    sys.exit(app.exec_())