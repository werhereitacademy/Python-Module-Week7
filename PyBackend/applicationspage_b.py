import os
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QTableWidgetItem
from collections import defaultdict

# PyFiles ve PyModules klasörlerini arama yoluna ekleme
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "PyFiles")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../PyModules")))

from applicationspage import Ui_Dialog  # UI dosyasını içe aktarıyoruz
import googledrive_m  # Google Drive'dan veri indirme modülü


class ApplicationsWindow(QDialog, Ui_Dialog):
    def __init__(self,role=None):
        super().__init__()
        self.setupUi(self)  # UI öğelerini oluştur
        self.users = self.load_users()  # Kullanıcı verilerini yükle
        self.populate_table()  # Tabloyu doldur
        self.role = role  # Kullanıcının rolünü sakla

        # Butonların tıklama işlemleri
        self.pushButton_dublicatereg.clicked.connect(self.show_duplicates)
        self.pushButton_appfiltered.clicked.connect(self.show_filtered)
        self.pushButton_allapp.clicked.connect(self.show_all)
        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_defined.clicked.connect(self.show_defined)  
        self.pushButton_unidentified.clicked.connect(self.show_unidentified)
        self.pushButton_preferences.clicked.connect(self.go_to) 
        self.pushButton_exit.clicked.connect(self.close)
        self.pushButton_differentreg.clicked.connect(self.show_different_vit)
        self.pushButton_previous_control.clicked.connect(self.show_non_vit3)

    def load_users(self):
        """Google Drive'dan kullanıcıları indir ve liste formatında sakla."""
        try:
            users = googledrive_m.download_xlsx_with_service_account(1)
            print(users)

            if isinstance(users, list) and all(isinstance(row, list) and len(row) >= 21 for row in users):
                return users
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "User data format is incorrect or missing columns!")
                return []
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load users: {e}")
            return []

    def populate_table(self, users=None):
        """TableWidget'i kullanıcı verileriyle doldur."""
        if users is None:
            users = self.users
        
        if not users:
            QtWidgets.QMessageBox.warning(self, "Warning", "No user data available!")
            return

        self.tableWidget.setRowCount(len(users))  # Satır sayısını ayarla
        self.tableWidget.setColumnCount(8)  # İlk 8 niteliği göstereceğimiz için 8 sütun ayarla

        for row_idx, user_data in enumerate(users):  # self.users listesindeki her bir kullanıcı için döngü
            for col_idx in range(8):  # İlk 8 niteliği almak için 0'dan 7'ye kadar dönen döngü
                item = QTableWidgetItem(str(user_data[col_idx]))  # Kullanıcı verisini QTableWidgetItem nesnesine çevir
                self.tableWidget.setItem(row_idx, col_idx, item)  # TableWidget içindeki ilgili hücreye yerleştir

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
        search_term = self.lineEdit_search.text().strip().lower()  # Arama terimini al

        if not search_term:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter a search term!")
            return

        # İsim-soyisime göre arama yap
        filtered_users = [user for user in self.users if search_term in user[1].lower()]

        if filtered_users:
            self.populate_table(filtered_users)  # Arama sonucunu tabloya yansıt
        else:
            QtWidgets.QMessageBox.information(self, "No Results", "No users found matching the search term.")


    def show_defined(self):
        """Google Drive'dan gelen verilerde 20. sütunda 'OK' yazanları filtrele."""

        defined_users = [user for user in self.users if len(user) > 20 and str(user[20]).strip().upper() == "OK"]

        if defined_users:
            self.populate_table(defined_users)  # Mentor atanmışları tabloya ekle
        else:
            QtWidgets.QMessageBox.information(self, "No Results", "No users with mentor assigned found.")

    def show_unidentified(self):
        """Google Drive'dan gelen verilerde 20. sütunda 'ATANMADI' yazanları filtrele."""

        unidentified_users = [user for user in self.users if len(user) > 20 and str(user[20]).strip().upper() == "ATANMADI"]

        if unidentified_users:
            self.populate_table(unidentified_users)  # Mentor atanmamışları tabloya ekle
        else:
            QtWidgets.QMessageBox.information(self, "No Results", "No users without mentor assignment found.")
    
    def go_to(self): 
        self.close()  # Mevcut pencereyi kapat

        if self.role == "admin":
            import pre_adminmenu_b  
            self.admin_menu = pre_adminmenu_b.AdminMenu()  # Admin pencere nesnesi oluştur
            self.admin_menu.show()
        else:
            import pre_usermenu_b  
            self.user_menu = pre_usermenu_b.UserMenu()  # Kullanıcı menüsü nesnesi oluştur
            self.user_menu.show()

    def show_different_vit(self):
        """Sadece 'VIT3' olanları göster, ama içinde 'VIT1' veya 'VIT2' olanları çıkar."""
        vit3_users = [user for user in self.users if len(user) > 20 and str(user[21]).strip().upper() == "VIT3"]  # 21. sütun (index 20)
        

        # 'VIT3' olanlar içinden 'VIT1' ve 'VIT2' içerenleri çıkart
        filtered_users = []
        for user in vit3_users:
            vit_column = " ".join(map(str, user))  # Tüm sütunları string olarak birleştir
            if "VIT1" not in vit_column and "VIT2" not in vit_column:
                filtered_users.append(user)

        print("Sadece 'VIT3' içerenler:", filtered_users)  # Debug için yazdır
        self.populate_table(filtered_users)
    
    def show_non_vit3(self):
        """21. sütunda 'VIT3' dışında kalanları listele."""
        non_vit3_users = [user for user in self.users if len(user) > 20 and str(user[21]) != "VIT3"]  # 21. sütun (index 20)

        print("VIT3 olmayanlar:", non_vit3_users)  # Debug için yazdır
        self.populate_table(non_vit3_users)    
            



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplicationsWindow()
    window.show()
    sys.exit(app.exec())
