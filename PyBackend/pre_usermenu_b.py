import sys
import os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog

# PyFiles klasörünü Python'un arama yoluna ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "PyFiles")))

from pre_usermenu import Ui_Dialog  
from applicationspage_b import ApplicationsWindow  # ApplicationsWindow'u içe aktarıyoruz

class UserMenu(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_applications.clicked.connect(self.open_applications)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_main.clicked.connect(self.go_to_login)

    def open_applications(self):
        """Applications penceresini açarken user rolünü gönder"""
        self.applications_window = ApplicationsWindow("user")
        self.applications_window.show()
        self.close()  # Mevcut pencereyi kapat
    def go_to_login(self):
        """Ana menüye dön: Çıkış yap ve login ekranına yönlendir."""
        self.close()  # Mevcut pencereyi kapat
        from login_b import LoginWindow  
        self.login_window = LoginWindow()  
        self.login_window.show()      

if __name__ == "__main__":
    app = QApplication([])
    window = UserMenu()
    window.show()
    app.exec()
