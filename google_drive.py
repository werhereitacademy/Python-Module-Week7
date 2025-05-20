# from googleapiclient.discovery import build
# from googleapiclient.http import MediaIoBaseDownload
# from google.oauth2 import service_account
# import pandas as pd
# import os
# import io

# # Yetkilendirme bilgileri
# SCOPES = ["https://www.googleapis.com/auth/drive"]
# SERVICE_ACCOUNT_FILE = "snm.json"  # JSON dosyanızın doğru yolu

# class GoogleDriveAPI:
#     def __init__(self, folder_id):
#         self.folder_id = folder_id
#         self.credentials = service_account.Credentials.from_service_account_file(
#             SERVICE_ACCOUNT_FILE, scopes=SCOPES
#         )
#         self.service = build("drive", "v3", credentials=self.credentials)

#     def list_files(self):
#         """Google Drive'daki belirli bir klasördeki dosyaları listeler."""
#         query = f"'{self.folder_id}' in parents and mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'"
#         results = self.service.files().list(q=query).execute()
#         files = results.get("files", [])
        
#         if not files:
#             print("📂 Klasörde hiçbir dosya bulunamadı.")
#         else:
#             print("📂 Klasördeki Dosyalar:")
#             for file in files:
#                 print(f"📄 {file['name']} (ID: {file['id']})")
        
#         return files

#     def download_file(self, file_id, file_name):
#         """Google Drive'dan belirli bir dosyayı indirir."""
#         request = self.service.files().get_media(fileId=file_id)
#         file_path = os.path.join("downloads", file_name)
#         os.makedirs("downloads", exist_ok=True)

#         with open(file_path, "wb") as f:
#             downloader = MediaIoBaseDownload(f, request)
#             done = False
#             while not done:
#                 status, done = downloader.next_chunk()
#                 print(f"⬇️ {file_name} indiriliyor... {int(status.progress() * 100)}% tamamlandı.")

#         return file_path

#     def read_excel(self, file_path):
#         """Excel dosyasını terminalde gösterir."""
#         try:
#             df = pd.read_excel(file_path, engine="openpyxl")  # 📌 OpenPyXL motorunu kullan
#             print("\n📂 Dosya içeriği:\n", df.head())  # İlk 5 satırı göster
#         except Exception as e:
#             print(f"❌ Hata: {e}")

#     def convert_excel_to_json(self, file_path):
#         """İndirilen Excel dosyasını JSON formatına çevirir ve kaydeder."""
#         if os.path.exists(file_path):
#             df = pd.read_excel(file_path, engine="openpyxl")
#             json_file_path = file_path.replace(".xlsx", ".json")
#             df.to_json(json_file_path, orient="records", indent=4, force_ascii=False)
#             print(f"✅ {json_file_path} oluşturuldu.")
#         else:
#             print(f"❌ {file_path} bulunamadı.")


from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
import pandas as pd
import os
import io

# Yetkilendirme bilgileri
SCOPES = ["https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = "snm.json"

class GoogleDriveAPI:
    def __init__(self, folder_id):
        self.folder_id = folder_id
        self.credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
        self.service = build("drive", "v3", credentials=self.credentials)

    def list_files(self):
        """Google Drive'daki belirli bir klasördeki dosyaları listeler."""
        query = f"'{self.folder_id}' in parents and mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'"
        results = self.service.files().list(q=query, orderBy="modifiedTime desc").execute()
        files = results.get("files", [])
        
        if not files:
            print("📂 Klasörde hiçbir dosya bulunamadı.")
            return None
        else:
            return files[0]  # En son güncellenen dosyayı döndür
    
    def download_file(self, file_id):
        """Google Drive'dan belirli bir dosyayı indirir ve bellekte tutar."""
        request = self.service.files().get_media(fileId=file_id)
        file_content = io.BytesIO()
        downloader = MediaIoBaseDownload(file_content, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()
        
        file_content.seek(0)  # Belleğin başına git
        return file_content

    def get_excel_as_list(self):
        """Google Drive'dan Excel dosyasını indirip liste olarak döndürür."""
        latest_file = self.list_files()
        if not latest_file:
            return None
        
        file_content = self.download_file(latest_file['id'])
        df = pd.read_excel(file_content, engine="openpyxl")
        
        return df.values.tolist()  # Liste formatında döndür

# Kullanım örneği
folder_id = "  "  # Klasör ID'sini buraya gir
gdrive = GoogleDriveAPI(folder_id)
data_list = gdrive.get_excel_as_list()

# if data_list:
#     print("✅ Veriler başarıyla alındı!")
#     print(data_list[:5])  # İlk 5 satırı göster
# else:
#     print("❌ Veri alınamadı.")