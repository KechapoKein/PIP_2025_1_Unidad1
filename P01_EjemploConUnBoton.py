import sys
from PyQt5 import uic, QtWidgets
qtCreatorfile = "P01_EjemploConUnBoton.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorfile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())