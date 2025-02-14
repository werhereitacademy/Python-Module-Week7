import pandas as pd
from PyQt6 import  QtWidgets
def read(file):
    

    # DataFrame okuma işlemi ve kontrol sadece bir kez yapılacak
    try:
        df = pd.read_excel("Files/"+file)  
        return df 
    except Exception as e:
        print(f"Hata: {e}")
        QtWidgets.QMessageBox.critical(None, "Hata", f"File did not read: {str(e)}")
        return None  # Dosya okunamazsa hata verir