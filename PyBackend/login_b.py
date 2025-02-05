import sys
import os
from PyQt6 import QtWidgets, QtGui

# login.py'nin bulunduğu PyFiles klasörünü import yoluna ekleyelim
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../PyFiles")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../PyModules")))

# login.py dosyasından Ui_Dialog sınıfını içe aktar
from login import Ui_Dialog
import pre_adminmenu_b  # Giriş admin ise yönlendirilecek sayfa
import pre_usermenu_b   # Giriş user ise yönlendirilecek sayfa
import googledrive_m    # Google Drive'dan veri indirme modülü


class LoginWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_login.clicked.connect(self.check_login)
        self.ui.pushButton_exit.clicked.connect(self.close)


        # Kullanıcı bilgilerini Google Drive'dan çekme
        self.users = self.load_users()

    def load_users(self):
        """Google Drive'dan kullanıcıları indir ve sözlüğe dönüştür."""
        try:
            users = googledrive_m.download_xlsx_with_service_account(2)
            if isinstance(users, dict):  # Eğer veriler sözlük formatındaysa doğrudan döndür
                return users
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "User data format is incorrect!")
                return {}
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load users: {e}")
            return {}

    def check_login(self):
        username = self.ui.lineEdit_username.text().strip()
        password = self.ui.lineEdit_password.text().strip()

        if username in self.users and self.users[username].get("password") == password:
            role = self.users[username].get("role", "user")
            QtWidgets.QMessageBox.information(self, "Success", f"Login successful! Role: {role}")
            self.open_menu(role)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid username or password!")

    def open_menu(self, role):
        """Yetkiye göre uygun pencereyi açar."""
        try:
            if role == "admin":
                if hasattr(pre_adminmenu_b, "AdminMenu"):
                    self.admin_menu = pre_adminmenu_b.AdminMenu()
                    self.admin_menu.show()
                else:
                    QtWidgets.QMessageBox.critical(self, "Error", "Admin menu could not be loaded!")

            elif role == "user":
                if hasattr(pre_usermenu_b, "UserMenu"):
                    self.user_menu = pre_usermenu_b.UserMenu()
                    self.user_menu.show()
                else:
                    QtWidgets.QMessageBox.critical(self, "Error", "User menu could not be loaded!")

            self.close()  # Giriş ekranını kapat

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to open menu: {e}")

def start_login_app():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    start_login_app()
