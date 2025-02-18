
from google_drive import GoogleDriveAPI
from PyQt6.QtWidgets import QApplication
from input_python import LoginPage

# Google Drive klasör ID'si
FOLDER_ID = "    "
def main():
    # Google Drive işlemleri başlatılıyor
    print("Google Drive işlemleri başlatılıyor...")
    drive = GoogleDriveAPI(FOLDER_ID)
    files = drive.list_files()

    # Listelenen dosyaları yazdırarak kontrol edelim
    print("Dosyalar:", files)

    # Dosya listesi içinde dönmeye çalışalım
    for file in files:
        print("Mevcut dosya:", file)
        # Eğer file bir sözlükse, 'name' ve 'id' kullanabiliriz
        if isinstance(file, dict):
            file_name = file.get("name")
            file_id = file.get("id")
            if file_name and file_id:
                file_path = drive.download_file(file_id, file_name)
                drive.read_excel(file_path)
                drive.convert_excel_to_json(file_path)
            else:
                print("Geçerli dosya bilgisi yok.")
        else:
            print("Dosya formatı hatalı:", file)

    print("Google Drive işlemleri tamamlandı. PyQt6 uygulaması başlatılıyor...")

    app = QApplication([])
    pencere = LoginPage()  # LoginPage, PyQt6 uygulamanızın ilk sayfası
    pencere.show()
    app.exec()  # exec() fonksiyonu ile PyQt uygulamasını başlatıyoruz


if __name__ == "__main__":
    main()