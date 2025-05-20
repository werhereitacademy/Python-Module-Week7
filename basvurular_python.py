import os
import sys
import json
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QTableWidgetItem
from basvurular import Ui_MainWindow as BasvurularUi
from prefences_python import PreferencesPage  # Kullanıcı tercihler sayfası
from prefences_admin_python import AdminPreferencesPage  # Admin tercihler sayfası
from collections import defaultdict

# PyFiles ve PyModules klasörlerini arama yoluna ekleme
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "PyFiles")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../PyModules")))

from google_drive import GoogleDriveAPI  # Google Drive'dan veri indirme modülü


class ApplicationsWindow(QtWidgets.QMainWindow):
    def __init__(self, role=None):
        super().__init__()
        self.role = role  # Parametreyi saklıyoruz
        self.ui = BasvurularUi()
        self.ui.setupUi(self)

        # Rol kontrolü (admin ya da user)
        if self.role == "admin":
            print("Admin olarak giriş yapıldı.")
        elif self.role == "user":
            print("Kullanıcı olarak giriş yapıldı.")
        else:
            print("Role belirtilmemiş.")


        # Butonların tıklama işlemleri
        self.ui.pushButton_duplicate.clicked.connect(self.show_duplicates)
        self.ui.pushButton_filter.clicked.connect(self.show_filtered)
        self.ui.pushButton_all_app.clicked.connect(self.show_all)
        self.ui.pushButton_search.clicked.connect(self.search)
        self.ui.pushButton_assigned.clicked.connect(self.show_defined)  
        self.ui.pushButton_unassigned.clicked.connect(self.show_unidentified)
        self.ui.pushButton_prefences.clicked.connect(self.go_back) 
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_unique.clicked.connect(self.show_different_vit)
        self.ui.pushButton_previous_vit.clicked.connect(self.show_non_vit3)

        # Google Drive API ile veri al
        self.gdrive = GoogleDriveAPI("12wqa_UOJIWIcF7fcf0Sd06M9Ey2LxwbS")  # Klasör ID'sini buraya ekleyin
        self.users = self.load_data_from_drive()


        # # JSON verisini yüklemek için değişkenler
        # self.data = []
        # self.headers = []
        # self.file_path = "downloads/Basvurular.json"

    def load_data_from_drive(self):
        """Google Drive'dan veriyi alır ve tabloyu doldurur."""
        data_list = self.gdrive.get_excel_as_list()  # Google Drive'dan Excel verisini al

        if not data_list:
            QtWidgets.QMessageBox.warning(self, "Hata", "Veriler alınamadı!")
            return []

        return data_list

    def load_all_meetings(self):
        """Verileri tabloya yükler."""
        if not self.users:
            print("Veriler boş!")
            return

        # Başlıkları ayarla
        self.headers = ['ID', 'Ad', 'Soyad', 'Email', 'Telefon', 'Durum']  # Örnek başlıklar, veriye göre güncelleyebilirsiniz
        self.ui.tableWidget.setColumnCount(len(self.headers))
        self.ui.tableWidget.setHorizontalHeaderLabels(self.headers)

        # Verileri tabloya ekle
        self.populate_table(self.users)

    def populate_table(self, data):
        """Tabloyu verilen veriyle doldurur."""
        self.ui.tableWidget.setRowCount(0)  # Önce tabloyu temizle
        self.ui.tableWidget.setRowCount(len(data))

        for row, user in enumerate(data):
            for col, value in enumerate(user):
                self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))

    def show_duplicates(self):
        """Aynı isim ve mail adresiyle kayıtlı kullanıcıları filtrele."""
        duplicates = defaultdict(list)

        # İsim ve mail adresine göre kullanıcıları grupla
        for user in self.users:
            name, email = user[1], user[2]
            duplicates[(name, email)].append(user)

        # Tekrar eden kayıtları seç
        duplicate_users = [users[1] for users in duplicates.values() if len(users) > 1]

        self.populate_table(duplicate_users)  # Tekrar eden kullanıcıları tabloya ekle

    def show_filtered(self):
        """Tekrar eden kayıtları hariç tutarak kullanıcıları filtrele."""
        unique_users = {}
        
        # İsim ve mail adresine göre kullanıcıları filtrele
        for user in self.users:
            name, email = user[1], user[2]
            if (name, email) not in unique_users:
                unique_users[(name, email)] = user

        # Filtrelenmiş kullanıcıları tabloya ekle
        self.populate_table(list(unique_users.values()))

    def show_all(self):
        """Tüm kullanıcı verilerini tekrar göster."""
        self.populate_table(self.users)  # Tüm veriyi tabloya ekle

    def search(self):
        """LineEdit'teki arama terimine göre isim ve soyisimlerde arama yap."""
        search_term = self.ui.lineEdit_basvurular.text().strip().lower()  # Arama terimini al

        if not search_term:
            QtWidgets.QMessageBox.warning(self, "Warning", "Lütfen bir arama terimi girin!")
            return

        # Kullanıcı listesini kontrol edelim
        print("Toplam Kullanıcı Sayısı:", len(self.users))
        print("İlk Kullanıcı Verisi:", self.users[0] if self.users else "Kullanıcı bulunamadı!")

        # Eğer kullanıcı listesi listelerden oluşuyorsa, Adınızı Soyadınızı kısmı user[0] olabilir
        filtered_users = [
            user for user in self.users if search_term in str(user[0]).lower()
        ]
        
        print("Bulunan Kullanıcılar:", filtered_users)  # Arama sonuçlarını terminale yazdır

        if filtered_users:
            self.populate_table(filtered_users)  # Arama sonucunu tabloya yansıt
        else:
            QtWidgets.QMessageBox.information(self, "Sonuç Yok", "Arama terimiyle eşleşen kullanıcı bulunamadı.")




    def show_defined(self):
        """Google Drive'dan gelen verilerde 20. sütunda 'OK' yazanları filtrele."""
        defined_users = [user for user in self.users if len(user) > 20 and str(user[20]).strip().upper() == "OK"]

        if defined_users:
            self.populate_table(defined_users)  # Mentor atanmışları tabloya ekle
        else:
            QtWidgets.QMessageBox.information(self, "Sonuç Yok", "Mentör atanmış kullanıcı bulunamadı.")

    def show_unidentified(self):
        """Google Drive'dan gelen verilerde 20. sütunda 'ATANMADI' yazanları filtrele."""
        unidentified_users = [user for user in self.users if len(user) > 20 and str(user[20]).strip().upper() == "ATANMADI"]

        if unidentified_users:
            self.populate_table(unidentified_users)  # Mentor atanmamışları tabloya ekle
        else:
            QtWidgets.QMessageBox.information(self, "Sonuç Yok", "Mentör atanması yapılmamış kullanıcı bulunamadı.")
    
    
    def show_different_vit(self):
        """Sadece 'VIT3' olanları göster, ama içinde 'VIT1' veya 'VIT2' olanları çıkar."""
        vit3_users = [user for user in self.users if len(user) > 20 and str(user[21]).strip().upper() == "VIT3"]

        # 'VIT3' olanlar içinden 'VIT1' ve 'VIT2' içerenleri çıkart
        filtered_users = []
        for user in vit3_users:
            vit_column = " ".join(map(str, user))  # Tüm sütunları string olarak birleştir
            if "VIT1" not in vit_column and "VIT2" not in vit_column:
                filtered_users.append(user)

        print("Sadece 'VIT3' içerenler:", filtered_users)  # Debug için yazdır
        self.populate_table(filtered_users)
    

    def go_back(self):
        print(f"Geri dönme işlemi başlatıldı. Rol: {self.role}")  # Debugging
        self.close()

        if self.role == "admin":
            print("Admin paneline yönlendiriliyor...")  # Debugging
            import prefences_admin_python
            self.admin_preferences = prefences_admin_python.AdminPreferencesPage()
            self.admin_preferences.show()
            print("Admin sayfasına geri dönüldü.")  # Debugging
        else:
            print("Kullanıcı paneline yönlendiriliyor...")  # Debugging
            import prefences_python
            self.user_preferences = prefences_python.PreferencesPage()
            self.user_preferences.show()
            print("Kullanıcı sayfasına geri dönüldü.")  # Debugging



    def show_non_vit3(self):
        """21. sütunda 'VIT3' dışında kalanları listele."""
        non_vit3_users = [user for user in self.users if len(user) > 20 and str(user[21]) != "VIT3"]

        print("VIT3 olmayanlar:", non_vit3_users)  # Debug için yazdır
        self.populate_table(non_vit3_users)    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplicationsWindow()
    window.show()
    sys.exit(app.exec())


