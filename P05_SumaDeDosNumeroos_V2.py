import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P05_SumaDeDosNumeroos_V2.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_sumar.clicked.connect(self.suma)

    # Área de los Slots
    def suma(self):
        try:
            num1 = float(self.txt_A.text())
            num2 = float(self.txt_B.text())
            sum = num1 + num2
            #self.msj("La suma de los numeros es: " + str(sum))
            self.txt_resultado.setText(str(sum))
        except Exception as error:
            print(error)

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

