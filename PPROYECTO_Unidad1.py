import sys
import pandas as pd
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt6 import uic


class DataAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("PROYECTO_Unidad1.ui", self)

        # Conectar botones a funciones
        self.btnLoad.clicked.connect(self.load_data)
        self.btnSave.clicked.connect(self.save_data)
        self.btnAnalyze.clicked.connect(self.analyze_data)
        self.btnLoadResults.clicked.connect(self.load_results)
        self.btnAddNumber.clicked.connect(self.add_number)

        self.data = []  # Lista para almacenar los datos

    def add_number(self):
        """ Agrega un número ingresado por el usuario a la lista """
        num_text = self.inputNumber.text().strip()
        if not num_text:
            QMessageBox.warning(self, "Error", "Ingrese un número antes de agregar.")
            return
        try:
            num = float(num_text)
            self.data.append(num)
            self.textEdit_2.setText(str(self.data))  # Mostrar la lista actualizada
            self.inputNumber.clear()
        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese un número válido.")

    def load_data(self):
        """ Carga un archivo de datos CSV """
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo", "", "CSV Files (*.csv)")
        if file_name:
            try:
                df = pd.read_csv(file_name)
                self.data = df['Valores'].tolist()
                self.textEdit_2.setText(str(self.data))
                QMessageBox.information(self, "Éxito", "Datos cargados correctamente")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al cargar el archivo: {e}")

    def save_data(self):
        """ Guarda los datos en un archivo CSV """
        file_name, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo", "", "CSV Files (*.csv)")
        if file_name:
            try:
                df = pd.DataFrame({'Valores': self.data})
                df.to_csv(file_name, index=False)
                QMessageBox.information(self, "Éxito", "Datos guardados correctamente")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al guardar el archivo: {e}")

    def analyze_data(self):
        """ Realiza análisis estadístico y guarda los resultados """
        if not self.data:
            QMessageBox.warning(self, "Advertencia", "No hay datos cargados para analizar")
            return

        if len(self.data) < 2:
            QMessageBox.warning(self, "Advertencia", "Se necesitan al menos dos valores para calcular varianza y desviación estándar.")
            return

        data_array = np.array(self.data)
        results = {
            "Valor Menor": np.min(data_array),
            "Valor Mayor": np.max(data_array),
            "Media": np.mean(data_array),
            "Mediana": np.median(data_array),
            "Moda": pd.Series(data_array).mode()[0] if not pd.Series(data_array).mode().empty else "No hay moda",
            "Desviación Estándar": np.std(data_array, ddof=1),
            "Varianza": np.var(data_array, ddof=1)
        }

        results_text = "\n".join([f"{key}: {value:.4f}" if isinstance(value, (int, float)) else f"{key}: {value}" for key, value in results.items()])
        self.textEditResults_2.setText(results_text)

        # Guardar los resultados automáticamente en un archivo
        try:
            pd.DataFrame([results]).to_csv("resultados.csv", index=False)
            QMessageBox.information(self, "Éxito", "Resultados guardados en 'resultados.csv'")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al guardar los resultados: {e}")

    def load_results(self):
        """ Carga un archivo con los resultados del análisis """
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo de Resultados", "", "CSV Files (*.csv)")
        if file_name:
            try:
                df = pd.read_csv(file_name)
                self.textEditResults_2.setText(df.to_string(index=False))
                QMessageBox.information(self, "Éxito", "Resultados cargados correctamente")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al cargar los resultados: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataAnalyzer()
    window.show()
    sys.exit(app.exec())
