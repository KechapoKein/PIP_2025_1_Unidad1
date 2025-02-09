import sys
from PyQt5 import uic, QtWidgets
qtCreatorfile = "P00_Introduccion.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorfile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def _init_(self):
        QtWidgets.QMainWindow._init_(self)
        Ui_MainWindow._init_(self)
        self.setupUi(self)

if __name__  == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
