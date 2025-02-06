import sys
import os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog

# PyFiles klasörünü Python'un arama yoluna ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "PyFiles")))
# pre_adminmenu.py içindeki Ui_Dialog sınıfını içe aktar
from pre_adminmenu import Ui_Dialog  

class AdminMenu(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)  # Arayüzü yükle

        # applicationspage_b.py dosyasındaki pencereyi açacak butonu bağla
        self.ui.pushButton_applications.clicked.connect(self.open_applications)
        self.ui.pushButton_exit.clicked.connect(self.close)

    def open_applications(self):
        """Applications penceresini açar"""
        from applicationspage_b import ApplicationsWindow 
        self.applications_window = ApplicationsWindow()
        self.applications_window.show()
      

if __name__ == "__main__":
    app = QApplication([])
    window = AdminMenu()
    window.show()
    app.exec()