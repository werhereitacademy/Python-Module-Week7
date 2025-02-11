import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
from googleapiclient.http import MediaIoBaseDownload
import io


SCOPES = ["https://www.googleapis.com/auth/drive"]
CREDS_DIR = "Cred"
TOKEN_PATH = os.path.join(CREDS_DIR, "token.json")
CREDENTIALS_PATH = os.path.join(CREDS_DIR, "credentials.json") #You must use your own credentials Check out the Cred Files

def download():
  """Shows basic usage of the Drive v3 API.
  Prints the names and ids of the first 10 files the user has access to.
  """
  creds = None
  
  if os.path.exists(TOKEN_PATH):
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          CREDENTIALS_PATH, SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open(TOKEN_PATH, "w") as token:
      token.write(creds.to_json())

  try:
    service = build("drive", "v3", credentials=creds)

    print("Connected")
  except HttpError as error:
    # TODO(developer) - Handle errors from drive API.
    print(f"An error occurred: {error}")



  def download_files():
    
    try:
        os.makedirs("Files", exist_ok=True)  
        FOLDER_ID="1h_HMM_k5JYqJ8Bz71bAAHfdM2CL7MiUF"
      
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

            
            request = service.files().get_media(fileId=file_id)
            with open(file_path, "wb") as file:
                downloader = MediaIoBaseDownload(file, request)
                done = False
                while not done:
                    _, done = downloader.next_chunk()

            print(f"Downloaded: {file_path}")

    except HttpError as error:
        print(f"An error occurred: {error}")

  download_files()
if __name__ == "__main__":
  download()