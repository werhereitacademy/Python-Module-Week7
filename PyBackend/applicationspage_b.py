import os
from PyQt6.QtWidgets import QApplication, QDialog
import sys
# PyFiles klasörünü Python'un arama yoluna ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "PyFiles")))

from applicationspage import Ui_Dialog  # applicationspage.py dosyasını içe aktarıyoruz

class ApplicationsWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # UI öğelerini oluştur

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplicationsWindow()
    window.show()
    sys.exit(app.exec())
