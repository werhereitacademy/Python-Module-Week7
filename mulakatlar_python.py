
import sys
import json
from PyQt6 import QtWidgets, uic
from datetime import datetime, timezone

from prefences_python import PreferencesPage  # Kullanıcı tercihler sayfası
from prefences_admin_python import AdminPreferencesPage  # Admin tercihler sayfası

class MulakatlarWindow(QtWidgets.QMainWindow):
    def __init__(self,role=None):
        super().__init__()
        self.role = role
        print(f"Role: {self.role}")  # Debugging amaçlı role değerini yazdırıyoruz
        uic.loadUi("mulakatlar.ui", self)
        self.setWindowTitle("Mulakatlar Uygulaması")
        self.setGeometry(300, 300, 800, 600)
        
        self.preferences_admin_window = None

        if self.role == "admin":
            print("Admin olarak giriş yapıldı.")
        elif self.role == "user":
            print("Kullanıcı olarak giriş yapıldı.")
        else:
            print("Role belirtilmemiş.")

        self.pushButton_mulakat_search.clicked.connect(self.ara_isim_soyisim)
        self.pushButton_submitted.clicked.connect(self.proje_gonderilmis_olanlar)
        self.pushButton_received.clicked.connect(self.proje_gelmis_olanlar)
        self.pushButton_preferences.clicked.connect(self.tercihler_ekranina_geri_don)
        self.pushButton_exit.clicked.connect(self.uygulamadan_cik)

        self.dosya_yolu = "downloads/Mulakatlar.json"
        self.veriler = self.veri_yukle()

    def veri_yukle(self):
        try:
            with open(self.dosya_yolu, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Dosya bulunamadı.")
            return []
        except json.JSONDecodeError:
            print("JSON dosyası hatalı.")
            return []

    def guncelle_tablo(self, veriler):
        self.tableWidget_mulakat.setRowCount(0)
        for veri in veriler:
            row_position = self.tableWidget_mulakat.rowCount()
            self.tableWidget_mulakat.insertRow(row_position)

            self.tableWidget_mulakat.setItem(row_position, 0, QtWidgets.QTableWidgetItem(veri['Adınız Soyadınız']))
            self.tableWidget_mulakat.setItem(row_position, 1, QtWidgets.QTableWidgetItem(self.timestamp_to_date(veri.get('Proje gonderilis tarihi'))))
            self.tableWidget_mulakat.setItem(row_position, 2, QtWidgets.QTableWidgetItem(self.timestamp_to_date(veri.get('Projenin gelis tarihi'))))

    def timestamp_to_date(self, timestamp):
        if not timestamp:
            return "-"
        return datetime.fromtimestamp(timestamp / 1000, timezone.utc).strftime('%Y-%m-%d')

    def ara_isim_soyisim(self):
        arama_terimi = self.lineEdit_search.text().lower()

        arama_sonucu = [
            veri for veri in self.veriler if arama_terimi in veri['Adınız Soyadınız'].lower()
        ]

        self.guncelle_tablo(arama_sonucu)

    def proje_gonderilmis_olanlar(self):
        proje_gonderilmis_olanlar = [
            veri for veri in self.veriler if veri.get('Proje gonderilis tarihi') is not None
        ]

        self.guncelle_tablo(proje_gonderilmis_olanlar)

    def proje_gelmis_olanlar(self):
        proje_gelmis_olanlar = [
            veri for veri in self.veriler if veri.get('Projenin gelis tarihi') is not None
        ]

        self.guncelle_tablo(proje_gelmis_olanlar)

    def tercihler_ekranina_geri_don(self):
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



    def uygulamadan_cik(self):
        QtWidgets.QApplication.quit()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MulakatlarWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()