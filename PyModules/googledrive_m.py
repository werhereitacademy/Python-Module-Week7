#substantialismswd@gmail.com
#vypYSuJukahOQITu
#camachostelllr@hotmail.com

from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd
import io

def download_xlsx_with_service_account(sheet_name,file_id='1mQ-afXga-_aZ8UOq2rOfJND96nrBa8C6'):
    # Service account key JSON dosyasının yolu
    SERVICE_ACCOUNT_FILE = './asset/valued-door-449716-c2-66b51c2a0a47.json'
    
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

        # Read a specific sheet by index (0-based)
        df = pd.read_excel(io.BytesIO(file_content), sheet_name=0)
        # Convert DataFrame to list of lists (excluding headers)
        data_list = df.values.tolist()

        # If you want to include headers as the first row
        #data_list_with_headers = [df.columns.tolist()] + df.values.tolist()

        #print(data_list)  # Just the data rows
        # or
        #print(data_list_with_headers)  # Data rows with column headers as first row
        return data_list
    
    except Exception as e:
        print(f"Dosya indirilemedi: {e}")
        return None

# Kullanım
# excellist = download_xlsx_with_service_account(1) #sheet index
# print(excellist)