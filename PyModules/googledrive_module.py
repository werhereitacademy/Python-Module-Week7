#substantialismswd@gmail.com
#vypYSuJukahOQITu
#camachostelllr@hotmail.com

import pandas as pd

# Google Sheets dosyasının paylaşılabilir bağlantısını alın
# Örnek: https://docs.google.com/spreadsheets/d/<SHEET_ID>/edit?usp=sharing
# Bağlantıdaki <SHEET_ID> kısmını kullanacağız.

def ReadGoogleSheet(sheet_id):
    # CSV formatında verileri çekmek için URL oluşturun
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

    # Verileri pandas ile okuyun
    df = pd.read_csv(url)

    # Verileri ekrana yazdırın
    #print(df)

    return df

# Açıklamalar:
# sheet_id: Google Sheets dosyasının bağlantısındaki https://docs.google.com/spreadsheets/d/<SHEET_ID>/edit?usp=sharing kısmındaki <SHEET_ID> değerini kullanın.
#https://docs.google.com/spreadsheets/d/1mQ-afXga-_aZ8UOq2rOfJND96nrBa8C6/edit?usp=sharing&ouid=114812450035369013790&rtpof=true&sd=true
# url: Google Sheets dosyasını CSV formatında indirmek için kullanılan URL.
# pandas.read_csv(): CSV formatındaki verileri bir DataFrame'e dönüştürür.