# Import necessary libraries
from google.oauth2 import service_account  # For handling Google service account credentials
from googleapiclient.discovery import build  # For building Google API services
import pandas as pd  # For data manipulation and analysis
import io  # For handling input/output operations, especially in-memory streams

# Define a function to download an Excel file from Google Drive using a service account
def download_xlsx_with_service_account(sheet_name, file_id='1mQ-afXga-_aZ8UOq2rOfJND96nrBa8C6'):
    # Path to the service account JSON key file
    SERVICE_ACCOUNT_FILE = './asset/valued-door-449716-c2-39f522e83736.json'
    
    # Define the required scopes for accessing Google Drive API
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    
    # Load credentials from the service account file with the specified scopes
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    # Build the Google Drive service using the credentials
    service = build('drive', 'v3', credentials=creds)
    
    try:
        # Request the file content from Google Drive using the file ID
        request = service.files().get_media(fileId=file_id)
        file_content = request.execute()  # Execute the request and get the file content
        
        # Convert the file content into a pandas DataFrame using the specified sheet name
        df = pd.read_excel(io.BytesIO(file_content), sheet_name=sheet_name)  # sheet_name is used to specify the sheet
        
        # Convert the DataFrame into a list of lists (excluding headers)
        data_list = df.values.tolist()

        # Return the list of data
        return data_list
    
    except Exception as e:
        # Handle any exceptions that occur during the process
        print(f"File could not be downloaded: {e}")
        return None

# Example usage
# excellist = download_xlsx_with_service_account(sheet_name=1)  # Download data from the sheet at index 1
# print(excellist)  # Print the downloaded data