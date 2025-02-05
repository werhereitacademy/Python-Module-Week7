import sys
import os
from PyQt6 import QtWidgets

# PyFiles klasörünü Python'un arama yoluna ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "PyFiles")))

# pre_adminmenu.py içindeki Ui_Dialog sınıfını içe aktar
from pre_adminmenu import Ui_Dialog  

class AdminMenu(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)  # Arayüzü bu pencereye yükle

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = AdminMenu()
    window.show()
    app.exec()
