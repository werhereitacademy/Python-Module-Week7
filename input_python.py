
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from input import Ui_MainWindow  # Burada input.py dosyasındaki formu kullanıyoruz
import json
import sys
from prefences_python import PreferencesPage  # Kullanıcı tercihler sayfası
from prefences_admin_python import AdminPreferencesPage  # Admin tercihler sayfası

class LoginPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_MainWindow()
        self.loginform.setupUi(self)

        print("Giriş sayfası yüklendi!")  # Debug: Sayfa yüklendi mi?

        # Butonlara bağlantılar ekleyelim
        self.loginform.pushButton_login.clicked.connect(self.GirisYap)
        self.loginform.pushButton_login_exit.clicked.connect(self.close)  # Çıkış butonu pencereyi kapatacak

    def GirisYap(self):
        # Kullanıcı adı ve şifreyi al
        kullanici_adi = self.loginform.lineEdit_username.text().strip()  # 'self.ui' yerine 'self.loginform'
        sifre = self.loginform.lineEdit_password.text().strip()  # 'self.ui' yerine 'self.loginform'

        # Kullanıcı verilerini içeren JSON dosyasını oku
        kullanicilar_data = self.kullanici_verisini_oku()

        if not kullanicilar_data:
            self.show_message("Hata", "Kullanıcı verisi yüklenemedi!")
            return

        # Kullanıcı adı ve şifreyi kontrol et
        for kullanici in kullanicilar_data:
            if kullanici["kullanici"] == kullanici_adi and kullanici["parola"] == sifre:
                role = kullanici.get("yetki", "").lower()  # Role bilgisi küçük harfe çevrildi
                
                if role == "admin":
                    self.show_message("Başarı", "Logged in as Admin!")
                    self.admin_ekranina_gec()
                elif role == "user":
                    self.show_message("Başarı", "Logged in as User!")
                    self.user_ekranina_gec()
                else:
                    self.show_message("Hata", "Yetkisiz giriş!")
                return

        self.show_message("Hata", "Username or password is incorrect.")

    def kullanici_verisini_oku(self):
        """ Google Drive'dan indirilen Kullanicilar.json dosyasını okur. """
        dosya_yolu = "downloads/Kullanicilar.json"
        print("Dosya Yolu:", dosya_yolu)  # Debug: Dosya yolu doğru mu?

        try:
            with open(dosya_yolu, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            self.show_message("Hata", "Kullanıcılar.json file not found.")
        except json.JSONDecodeError:
            self.show_message("Hata", "Invalid JSON file.")

        return None

    def show_message(self, title, text):
        """ Kullanıcıya mesaj göstermek için fonksiyon. """
        message = QMessageBox()
        message.setWindowTitle(title)
        message.setText(text)
        message.exec()

    def admin_ekranina_gec(self):
        """ Admin ekranına yönlendirme """
        try:
            print("Admin Sayfası Açılıyor...")
            self.admin_page = AdminPreferencesPage()  # Parametreyi geçmeyin
            self.admin_page.show()
            print("Admin Sayfası Açıldı.")
            self.close()  # Giriş sayfasını kapat
        except Exception as e:
            print(f"Admin sayfasına yönlendirilirken hata oluştu: {e}")

    def user_ekranina_gec(self):
        """ Kullanıcı ekranına yönlendirme """
        try:
            print("User Sayfası Açılıyor...")  # Debug: User sayfası açılıyor mu?
            self.user_page = PreferencesPage()  # Parametresiz olarak yönlendiriyoruz
            self.user_page.show()
            print("User Sayfası Açıldı.")  # Debug: User sayfası açıldığında bu mesaj gelmeli
            self.close()  # Giriş sayfasını kapat
        except Exception as e:
            print(f"User sayfasına yönlendirilirken hata oluştu: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginPage()
    window.show()
    sys.exit(app.exec())