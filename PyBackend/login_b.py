import sys
import os
from PyQt6 import QtWidgets,QtGui,QtWidgets
# login.py'nin bulunduğu PyFiles klasörünü import yoluna ekleyelim
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../PyFiles")))
# login.py dosyasından Ui_Dialog sınıfını içe aktar
from login import Ui_Dialog
import pre_adminmenu_b  # Giriş admin ise yönlendirilecek sayfa
import pre_usermenu_b   # Giriş user ise yönlendirilecek sayfa
 

class LoginWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Butonları bağlama
        self.ui.pushButton_login.clicked.connect(self.check_login)
        self.ui.pushButton_exit.clicked.connect(self.close)

        # Kullanıcı bilgilerini içeren sözlük
        self.users = {
            "ahmet": {"password": "werhere", "role": "admin"},
            "mehmet": {"password": "itforever", "role": "user"},
            "selim": {"password": "cyber_warrior", "role": "user"}
        }

    def check_login(self):
        username = self.ui.lineEdit_username.text()
        password = self.ui.lineEdit_password.text()

        if username in self.users and self.users[username]["password"] == password:
            role = self.users[username]["role"]
            QtWidgets.QMessageBox.information(self, "Success", f"Login successful! Role: {role}")
            self.open_menu(role)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid username or password!")

    def open_menu(self, role):
        """Yetkiye göre uygun pencereyi açar."""
        if role == "admin":
            self.admin_menu = pre_adminmenu_b.AdminMenu()
            self.admin_menu.show()
        elif role == "user":
            self.user_menu = pre_usermenu_b.UserMenu()
            self.user_menu.show()
        
        self.close()  # Giriş ekranını kapat

def start_login_app():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    start_login_app()
