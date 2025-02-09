import sys
from PyQt5 import uic, QtWidgets
from fontTools.subset import prune_hints

qtCreatorFile = "P07_SumaDeMultiplesNumeros-load.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_cargar.clicked.connect(self.cargar)
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_guardar.clicked.connect(self.guardar)
        self.numeros = [] #lista vacia, que puede ser utilizada en cualquier parte de la clase

    # Área de los Slots
    def cargar(self):
        archivo = open("../Archivos/numeros.csv")
        contenido = archivo.readlines() #lee al archivo completo
        print(contenido)
        ##nums  = [float(i) for i in contenido]
        ###########################
        nums = []
        for i in contenido:
            nums.append(float(i))
        ###############
        print(nums)
        self.numeros = nums
        self.sumar()

    def agregar(self):
        try:
            num = float(self.txt_numero.text())
            self.numeros.append(num)
            self.sumar()
        except Exception as error:
            print(error)

    def guardar(self):
        archivo = open("../Archivos/numeros.csv","w")  # "w" = write / "a"  = append
        for num in self.numeros:
            archivo.write(str(num) + "\n")
        archivo.flush()
        archivo.close()
        self.msj("Archivo Guardado! :D")

    def sumar(self):
        sumaaa = sum(self.numeros)
        self.txt_suma.setText(str(sumaaa))


    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

