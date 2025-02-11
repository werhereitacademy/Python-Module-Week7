# admin_backend.py

import pandas as pd
from backend.readfile import read
 

def authenticate_user(username, password):
    
    df=read("Kullanicilar.xlsx")
    

    # DataFrame'de username ve password eşleşmesini kontrol et
    user_row = df[(df["kullanici"] == username) & (df["parola"] == password)]

    # Eğer kullanıcı ve şifre eşleşiyorsa
    if not user_row.empty:
        role = user_row.iloc[0]["yetki"]  # Kullanıcının rolünü al
        print(f"Kullanıcı {username} başarıyla giriş yaptı. Rolü: {role}")
        return True,role  # Başarılı giriş

    # Kullanıcı adı veya şifre yanlışsa
    print("Kullanıcı adı veya şifre yanlış.")
    return False ,None # Hatalı giriş

