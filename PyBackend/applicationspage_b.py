import os 
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QTableWidgetItem

# PyFiles ve PyModules klasörlerini arama yoluna ekleme
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "PyFiles")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../PyModules")))

from applicationspage import Ui_Dialog  # UI dosyasını içe aktırıyoruz
import googledrive_m  # Google Drive'dan veri indirme modülü

class ApplicationsWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.users = self.load_users()

        self.pushButton_allapp.clicked.connect(self.populate_table)
        self.pushButton_dublicatereg.clicked.connect(self.show_duplicates)
        self.pushButton_appfiltered.clicked.connect(self.show_filtered)
        self.pushButton_exit.clicked.connect(self.close)

        self.populate_table()  # Pencere açıldığında verileri yükle

    def load_users(self):
        """Google Drive'dan kullanıcıları indir ve liste formatında sakla."""
        try:
            users = googledrive_m.download_xlsx_with_service_account(1)
            print(users)

            if isinstance(users, list) and all(isinstance(row, list) and len(row) >= 8 for row in users):
                return users
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "User data format is incorrect!")
                return []
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load users: {e}")
            return []

    def populate_table(self, data=None):
        """TableWidget'i verilen verilerle doldur."""
        # Veriyi her seferinde tekrar çekelim
        self.users = self.load_users()
        
        data = data if data is not None else self.users
        
        if not data:
            QtWidgets.QMessageBox.warning(self, "Warning", "No user data available!")
            return

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(8)

        for row_idx, user_data in enumerate(data):
            for col_idx in range(8):
                item = QTableWidgetItem(str(user_data[col_idx]))
                self.tableWidget.setItem(row_idx, col_idx, item)


    def show_duplicates(self):
        """Tekrar eden isim ve e-posta adreslerini göster."""
        seen = set()
        duplicates = []
        for user in self.users:
            identifier = (user[0], user[1])  # Ad ve E-posta
            if identifier in seen:
                duplicates.append(user)
            else:
                seen.add(identifier)
        self.populate_table(duplicates)

    def show_filtered(self):
        """Mükerrer kayıtlar olmadan, benzersiz kayıtları göster."""
        unique_users = []
        seen = set()
        for user in self.users:
            identifier = (user[0], user[1])  # Ad ve E-posta
            if identifier not in seen:
                unique_users.append(user)
                seen.add(identifier)
        self.populate_table(unique_users)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplicationsWindow()
    window.show()
    sys.exit(app.exec())
