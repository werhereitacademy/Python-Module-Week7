import os
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QTableWidgetItem

# PyFiles ve PyModules klasörlerini arama yoluna ekleme
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "PyFiles")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../PyModules")))

from applicationspage import Ui_Dialog  # UI dosyasını içe aktarıyoruz
import googledrive_m  # Google Drive'dan veri indirme modülü


class ApplicationsWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # UI öğelerini oluştur
        self.users = self.load_users()  # Kullanıcı verilerini yükle

        self.pushButton_allapp.clicked.connect(self.populate_table)
        self.pushButton_exit.clicked.connect(self.close)  # Çıkış butonu pencereyi kapatacak
        

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

    def populate_table(self):
        """TableWidget'i kullanıcı verileriyle doldur."""
        if not self.users:
            QtWidgets.QMessageBox.warning(self, "Warning", "No user data available!")
            return

        self.tableWidget.setRowCount(len(self.users))  # Satır sayısını ayarla
        self.tableWidget.setColumnCount(8)  # İlk 8 niteliği göstereceğimiz için 8 sütun ayarla

        for row_idx, user_data in enumerate(self.users):  # self.users listesindeki her bir kullanıcı için döngü
            for col_idx in range(8):  # İlk 8 niteliği almak için 0'dan 7'ye kadar dönen döngü
                item = QTableWidgetItem(str(user_data[col_idx]))  # Kullanıcı verisini QTableWidgetItem nesnesine çevir
                self.tableWidget.setItem(row_idx, col_idx, item)  # TableWidget içindeki ilgili hücreye yerleştir


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplicationsWindow()
    window.show()
    sys.exit(app.exec())
