import sys
import os
from PyQt6 import QtWidgets

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
