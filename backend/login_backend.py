import pandas as pd
from backend.readfile import read

def authenticate_user(username, password):
    """
    Kullanıcı adı ve şifre doğrulama fonksiyonu.
    Eğer kullanıcı doğrulanırsa, rolünü döndürür.
    """
    df = read("Kullanicilar.xlsx")

    # Eğer df boş veya None ise, giriş hatası döndür
    if df is None or df.empty:
        print("Kullanıcı veritabanı boş veya okunamadı.")
        return None, None

    # DataFrame'de username ve password eşleşmesini kontrol et
    user_row = df[(df["kullanici"] == username) & (df["parola"] == password)]

    # Eğer kullanıcı ve şifre eşleşiyorsa
    if not user_row.empty:
        role = user_row.iloc[0]["yetki"]  # Kullanıcının rolünü al
        print(f"Kullanıcı {username} başarıyla giriş yaptı. Rolü: {role}")
        return True, role  # Başarılı giriş

    # Kullanıcı adı veya şifre yanlışsa
    print("Kullanıcı adı veya şifre yanlış.")
    return False, None  # Hatalı giriş
