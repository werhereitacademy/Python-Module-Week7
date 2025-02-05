import sys
import os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog

# PyFiles klasörünü Python'un arama yoluna ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "PyFiles")))

# pre_adminmenu.py içindeki Ui_Dialog sınıfını içe aktar
from pre_adminmenu import Ui_Dialog  

# applicationspage_b.py dosyasını içe aktar
from applicationspage_b import ApplicationsWindow  # ApplicationsWindow sınıfını çağıracağız
from login_b import LoginWindow 

class AdminMenu(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)  # Arayüzü yükle

        self.ui.pushButton_applications.clicked.connect(self.open_applications)
        self.ui.pushButton_mainmenu.clicked.connect(self.open_login)
        self.ui.pushButton_exit.clicked.connect(self.close)

    def open_applications(self):
        """Applications penceresini açar"""
        self.applications_window = ApplicationsWindow()
        self.applications_window.show()
    def open_login(self):
        """Login penceresine geri döner"""
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()  # Admin menüyü kapat

if __name__ == "__main__":
    app = QApplication([])
    window = AdminMenu()
    window.show()
    app.exec()
