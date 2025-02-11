import os
import os.path
import io
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

# Google Drive erişimi için gerekli izinler
SCOPES = ["https://www.googleapis.com/auth/drive"]
CREDS_DIR = "Cred-"
TOKEN_PATH = os.path.join(CREDS_DIR, "token.json")
CREDENTIALS_PATH = os.path.join(CREDS_DIR, "credentials.json")

def download():
    """Google Drive'dan belirli dosyaları indirir ve hata yönetimini uygular."""
    creds = None
    try:
        # Önceden alınmış kimlik bilgileri olup olmadığını kontrol et
        if os.path.exists(TOKEN_PATH):
            creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

        # Kimlik bilgileri geçerli değilse, yenisini al
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
                creds = flow.run_local_server(port=0)

            # Yeni kimlik bilgisini kaydet
            with open(TOKEN_PATH, "w") as token:
                token.write(creds.to_json())

        # Google Drive servisine bağlan
        service = build("drive", "v3", credentials=creds)
        print("Connected to Google Drive.")

        download_files(service)  # Dosyaları indir

    except FileNotFoundError as e:
        print(f"Dosya bulunamadı hatası: {e}")
    except HttpError as e:
        print(f"Google Drive API hatası: {e}")
    except Exception as e:
        print(f"Bilinmeyen bir hata oluştu: {e}")

def download_files(service):
    """Belirtilen klasördeki Excel dosyalarını indirir."""
    try:
        os.makedirs("Files", exist_ok=True)  # Eğer yoksa "Files" klasörünü oluştur
        FOLDER_ID = "1h_HMM_k5JYqJ8Bz71bAAHfdM2CL7MiUF"  # Google Drive'daki hedef klasör

        # Klasördeki .xlsx dosyalarını bul
        query = f"'{FOLDER_ID}' in parents and mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'"
        results = service.files().list(q=query, fields="files(id, name)").execute()
        items = results.get("files", [])

        if not items:
            print("No .xlsx files found in CRM folder.")
            return

        for item in items:
            file_id = item["id"]
            file_name = item["name"]
            file_path = os.path.join("Files", file_name)

            # Dosyayı indir
            request = service.files().get_media(fileId=file_id)
            with open(file_path, "wb") as file:
                downloader = MediaIoBaseDownload(file, request)
                done = False
                while not done:
                    _, done = downloader.next_chunk()

            print(f"Downloaded: {file_path}")

    except HttpError as e:
        print(f"Google Drive API hatası: {e}")
    except OSError as e:
        print(f"Dosya işlemi hatası: {e}")
    except Exception as e:
        print(f"Bilinmeyen bir hata oluştu: {e}")

if __name__ == "__main__":
    download()