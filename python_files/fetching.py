from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io, os, json
import pandas as pd


SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
CLIENT_SECRETS_FILE = 'C:/Users/eren_/Desktop/CRM/python_files/credentials.json'
TOKEN_FILE = 'token.json'


if os.path.exists(TOKEN_FILE):
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
else:
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    with open(TOKEN_FILE, 'w') as token:
        token.write(creds.to_json())


service = build('drive', 'v3', credentials=creds)


folder_id = '1LFAU6uVOLzYatC5J_moXNOaNVL5SNGIt'


results = service.files().list(q=f"'{folder_id}' in parents", fields="files(id, name)").execute()
files = results.get('files', [])
for file in files:
    file_id = file['id']
    file_name = file['name']

    print(f"{file_name} dosyası indiriliyor...")

    # Dosyayı indir
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()

    fh.seek(0)


    df = pd.read_excel(fh, header=None)  

    
    print(f"{file_name} için algılanan sütun sayısı: {len(df.columns)}")
    print("İlk 5 satır:")
    print(df.head())

   
    expected_columns = ["Tarih", "Donem", "Aday Ismi", "Mentor", "Degerlendirme", "Dil Seviyesi"]

   
    if len(df.columns) == len(expected_columns):
        df.columns = expected_columns
    else:
        print(f"{file_name} dosyasında sütun sayısı uyuşmuyor. Otomatik düzenleniyor...")
        missing_columns = len(expected_columns) - len(df.columns)
        if missing_columns > 0:
            for i in range(missing_columns):
                df[f"Extra_Column_{i+1}"] = None 
        elif missing_columns < 0:
            df = df.iloc[:, :len(expected_columns)]  

        df.columns = expected_columns

    
    json_data = df.to_json(orient='records', lines=False, force_ascii=False)

    
    json_file_name = f'{file_name}.json'
    with open(json_file_name, 'w', encoding='utf-8') as json_file:
        json.dump(json.loads(json_data), json_file, indent=4, ensure_ascii=False)

    print(f"{file_name} JSON formatında {json_file_name} dosyasına yazıldı.")
