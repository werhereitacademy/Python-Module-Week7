import sys
import os
from PyQt6 import QtWidgets

# PyFiles klasörünü Python'un arama yoluna ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "PyFiles")))

# applicationspage.py içindeki Ui_Dialog sınıfını içe aktar
from applicationspage import Ui_Dialog  

class ApplicationsWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)  # Arayüzü bu pencereye yükle

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ApplicationsWindow()
    window.show()