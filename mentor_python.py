

import sys
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt6.QtCore import Qt
from mentor import Ui_MainWindow as MentorUi

from prefences_python import PreferencesPage  # Kullanıcı tercihler sayfası
from prefences_admin_python import AdminPreferencesPage  # Admin tercihler sayfası

class MentorApp(QMainWindow):
    def __init__(self, role=None):
        super().__init__()
        self.role = role  # Parametreyi saklıyoruz
        self.ui = MentorUi()
        self.ui.setupUi(self)

        if self.role == "admin":
            print("Admin olarak giriş yapıldı.")
        elif self.role == "user":
            print("Kullanıcı olarak giriş yapıldı.")
        else:
            print("Role belirtilmemiş.")


        # Butonlara işlev atama
        self.ui.pushButton_mentor_all_c.clicked.connect(self.load_all_meetings)
        self.ui.pushButton_mentor_search.clicked.connect(self.search_meeting)
        self.ui.pushButton_mentor_exit.clicked.connect(self.close_application)
        self.ui.pushButton_mentor_preferences.clicked.connect(self.go_back)  # Geri gitme işlevi
        self.ui.comboBox_mentor_search.currentIndexChanged.connect(self.filter_by_column)

        # JSON verisini yüklemek için değişkenler
        self.data = []
        self.headers = []
        self.file_path = "downloads/Mentor.json"

        # 🔹 İlk açılışta tabloyu boş bırak
        self.ui.tableWidget_mentor.setRowCount(0)



    def load_all_meetings(self):
        """JSON dosyasından tüm verileri yükler ve tabloya ekler."""
        try:
            with open(self.file_path, "r") as file:
                self.data = json.load(file)

            if not self.data:
                print("JSON dosyası boş!")
                return

            # Başlıkları ayarla
            self.headers = list(self.data[0].keys())
            self.ui.tableWidget_mentor.setColumnCount(len(self.headers))
            self.ui.tableWidget_mentor.setHorizontalHeaderLabels(self.headers)

            # Verileri tabloya ekle
            self.populate_table(self.data)

        except FileNotFoundError:
            print(f"Hata: {self.file_path} dosyası bulunamadı!")
        except json.JSONDecodeError:
            print(f"Hata: {self.file_path} okunamadı! Dosya bozuk olabilir.")

    def populate_table(self, data):
        """Tabloyu verilen veriyle doldurur."""
        self.ui.tableWidget_mentor.setRowCount(0)  # Önce tabloyu temizle
        self.ui.tableWidget_mentor.setRowCount(len(data))

        for row, meeting in enumerate(data):
            for col, key in enumerate(self.headers):
                value = str(meeting.get(key, ""))
                self.ui.tableWidget_mentor.setItem(row, col, QTableWidgetItem(value))

    def search_meeting(self):
        """Arama kutusuna girilen metne göre tabloyu filtreler."""
        if not self.data:
            print("Veri boş, JSON yükleniyor...")
            self.load_all_meetings()

        search_text = self.ui.lineEdit_mentor_search.text().strip().lower()
        if not search_text:
            print("Boş arama yapıldı, tüm veriler yükleniyor.")
            self.populate_table(self.data)
            return

        filtered_data = [
            row for row in self.data if any(search_text in str(value).lower() for value in row.values())
        ]

        if not filtered_data:
            print("Eşleşen kayıt bulunamadı.")
        self.populate_table(filtered_data)

    def filter_by_column(self):
        """ComboBox'tan seçilen değere göre tabloyu filtreler."""
        selected_text = self.ui.comboBox_mentor_search.currentText().strip().lower()

        if not self.data:
            print("Veri boş, yükleniyor...")
            self.load_all_meetings()

        if not selected_text:
            print("Boş seçim yapıldı, tüm veriler yükleniyor.")
            self.populate_table(self.data)
            return

        column_index = 5  # 6. sütunun index numarası
        if column_index >= len(self.headers):
            print("Hata: 6. sütun mevcut değil!")
            return
        
        column_key = self.headers[column_index]
        filtered_data = [row for row in self.data if str(row.get(column_key, "")).strip().lower() == selected_text]

        if not filtered_data:
            print(f"Eşleşen kayıt bulunamadı: {selected_text}")
        self.populate_table(filtered_data)



    def close_application(self):
        """Uygulamayı kapatır."""
        reply = QMessageBox.question(self, 'Uygulama Kapat', 'Uygulamayı kapatmak istiyor musunuz?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            QApplication.quit()


        
    def go_back(self):
        self.close()

        if self.role =="admin":
            import prefences_admin_python
            self.admin_preferences = prefences_admin_python.AdminPreferencesPage()
            self.admin_preferences.show()
            print("Admin sayfasına geri dönüldü.")  # Debugging
        else:
            import prefences_python
            self.user_preferences = prefences_python.PreferencesPage()
            self.user_preferences.show()
            print("Kullanıcı sayfasına geri dönüldü.")  # Debugging


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MentorApp()
    window.show()
    sys.exit(app.exec())

