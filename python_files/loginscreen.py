import json
import os
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont




# Global değişken tanımı
current_user_role = None

def load_users():
    """Kullanıcı bilgilerini JSON dosyasından okur."""
    json_file_path = "C:/Users/eren_/Desktop/CRM/coverted_files/Kullanicilar.json"  # JSON dosyasının tam yolu
    if not os.path.exists(json_file_path):
        return []  # Eğer dosya yoksa boş liste döndür
    
    with open(json_file_path, "r", encoding="utf-8") as file:
        return json.load(file)  # JSON dosyasını liste olarak oku

def get_user_role(username, password):
    """
    Verilen kullanıcı adı ve şifreye göre kullanıcının rolünü döner.
    Eğer kullanıcı bulunamazsa None döner.
    """
    users = load_users()
    for user in users:
        if user["kullanici"] == username and user["parola"] == password:
            return user["yetki"]
    return None

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Window")
        self.setFixedSize(400, 300)

        # Main widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Username label and input field
        self.label_username = QLabel("Username:")
        self.label_username.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.label_username)

        self.input_username = QLineEdit(self)
        self.input_username.setPlaceholderText("Enter your username")
        self.input_username.setFixedWidth(250)
        self.input_username.setStyleSheet(
            "padding: 5px; border: 1px solid #aaa; border-radius: 8px; font-size: 12px;"
        )
        self.layout.addWidget(self.input_username)

        # Password label and input field
        self.label_password = QLabel("Password:")
        self.label_password.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.label_password)

        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password.setPlaceholderText("Enter your password")
        self.input_password.setFixedWidth(250)
        self.input_password.setStyleSheet(
            "padding: 5px; border: 1px solid #aaa; border-radius: 8px; font-size: 12px;"
        )
        self.layout.addWidget(self.input_password)

        # Login button
        self.login_button = QPushButton("Login")
        self.login_button.setFixedWidth(120)
        self.login_button.setStyleSheet(
            """
            QPushButton {
                background-color: #5cb85c; color: white; border-radius: 10px; padding: 10px;
            }
            QPushButton:hover {
                background-color: #4cae4c;
            }
            QPushButton:pressed {
                background-color: #449d44;
            }
            """
        )

        self.login_button.clicked.connect(self.handle_login)
        self.layout.addWidget(self.login_button)

        # Uyarı label'ı
        self.warning_label = QLabel("")
        self.warning_label.setFont(QFont("Arial", 10))
        self.warning_label.setStyleSheet("color: red;")
        self.layout.addWidget(self.warning_label)

        # Çıkış butonu
        self.exit_button = QPushButton("Çıkış")
        self.exit_button.setFixedWidth(120)
        self.exit_button.setStyleSheet(
            """
            QPushButton {
                background-color: #d9534f; color: white; border-radius: 10px; padding: 10px;
            }
            QPushButton:hover {
                background-color: #c9302c;
            }
            QPushButton:pressed {
                background-color: #ac2925;
            }
            """
        )
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)

    def handle_login(self):
        """Giriş butonu tıklanıldığında çalışır."""
        username = self.input_username.text().strip()
        password = self.input_password.text().strip()

        # Kullanıcı rolünü belirleme
        global current_user_role
        current_user_role = get_user_role(username, password)

        if current_user_role:
            jsonPath = "C:/Users/eren_/Desktop/CRM/python_files/role.json"
            if current_user_role == "admin":
                QMessageBox.information(self, "Success", "Welcome! You have logged in as Admin.")
                self.redirect_to_admin()
                
                data = {"login":"admin"}
                with open(jsonPath, "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                
            else:
                QMessageBox.information(self, "Success", "Welcome! You have logged in as User.")
                self.redirect_to_user_preferences()
                
                data = {"login":"user"}
                with open(jsonPath, "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
        else:
            self.warning_label.setText("Incorrect username or password!")


    def redirect_to_admin(self):
        """Admin ekranına yönlendirme."""
        from PrefenceAdminMenu import Ui_Form_Admin
        self.admin_window = QWidget()
        self.ui = Ui_Form_Admin()
        self.ui.setupUi(self.admin_window)
        self.admin_window.show()  
        self.close()

    def redirect_to_user_preferences(self):
        """Kullanıcı tercihler ekranına yönlendirme."""
        from PrefenceMenu import Ui_Form
        self.user_window = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.user_window)
        self.user_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
