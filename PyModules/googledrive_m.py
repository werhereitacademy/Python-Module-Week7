#substantialismswd@gmail.com
#vypYSuJukahOQITu
#camachostelllr@hotmail.com

from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd
import io

def download_xlsx_with_service_account(sheet_name, file_id='1mQ-afXga-_aZ8UOq2rOfJND96nrBa8C6'):
    # Service account key JSON dosyasının yolu
    SERVICE_ACCOUNT_FILE = './asset/valued-door-449716-c2-39f522e83736.json'
    
    # Drive API için gerekli izinler
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    
    # Kimlik bilgilerini yükleme
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    # Drive servisini oluşturma
    service = build('drive', 'v3', credentials=creds)
    
    try:
        # Dosya içeriğini indirme
        request = service.files().get_media(fileId=file_id)
        file_content = request.execute()
        
        # Dosyayı bellek içinde DataFrame'e çevirme
        df = pd.read_excel(io.BytesIO(file_content), sheet_name=sheet_name)  # sheet_name parametresini kullandık

        # DataFrame'i listeye çevirme (başlıklar hariç)
        data_list = df.values.tolist()

        return data_list
    
    except Exception as e:
        print(f"Dosya indirilemedi: {e}")
        return None

# Kullanım
# excellist = download_xlsx_with_service_account(sheet_name=2)  # sheet index
# print(excellist)
