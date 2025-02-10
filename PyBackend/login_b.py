import sys
import os
from PyQt6 import QtWidgets

# login.py'nin bulunduğu PyFiles klasörünü import yoluna ekleyelim
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../PyFiles")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../PyModules")))

# login.py dosyasından Ui_Dialog sınıfını içe aktar
from login import Ui_Dialog

import googledrive_m    # Google Drive'dan veri indirme modülü


class LoginWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_login.clicked.connect(self.check_login)
        self.ui.pushButton_exit.clicked.connect(self.close)

        # Kullanıcı bilgilerini Google Drive'dan çekme (Liste formatında)
        self.users = self.load_users()
        

    def load_users(self):
        """Google Drive'dan kullanıcıları indir ve liste formatında sakla."""
        try:
            users = googledrive_m.download_xlsx_with_service_account(2)
            print(users)

            if isinstance(users, list) and all(isinstance(row, list) and len(row) >= 3 for row in users):
                return users
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "User data format is incorrect!")
                return []
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load users: {e}")
            return []

    def check_login(self):
        """Kullanıcı giriş bilgilerini kontrol et."""
        username = self.ui.lineEdit_username.text().strip()
        password = self.ui.lineEdit_password.text().strip()

        # Kullanıcıyı listede ara
        user_data = next((row for row in self.users if row[0] == username and row[1] == password), None)

        if user_data:
            role = user_data[2]  # Yetkiyi (role) al
            self.open_menu(role)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid username or password!")

    def open_menu(self, role):
        """Yetkiye göre uygun pencereyi açar."""
        try:
            if role == "admin":
                import pre_adminmenu_b  # Giriş admin ise yönlendirilecek sayfa
                self.admin_menu = pre_adminmenu_b.AdminMenu()
                self.admin_menu.show()

            elif role == "user":
                import pre_usermenu_b   # Giriş user ise yönlendirilecek sayfa
                self.user_menu = pre_usermenu_b.UserMenu()
                self.user_menu.show()

            self.close()  # Giriş ekranını kapat

        except AttributeError:
            QtWidgets.QMessageBox.critical(self, "Error", "Menu could not be loaded!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to open menu: {e}")


def start_login_app():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
