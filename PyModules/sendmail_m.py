import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_gmail(sender_email, sender_password, receiver_email, subject, body):
    # E-posta mesajını oluştur
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Mesaj gövdesini ekle
    message.attach(MIMEText(body, "plain"))

    try:
        # Gmail SMTP sunucusuna bağlan
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Güvenli bağlantı kur
            server.login(sender_email, sender_password)  # Giriş yap
            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)  # E-postayı gönder
        return ("E-posta başarıyla gönderildi!")
    except Exception as e:
        return (f"E-posta gönderilirken bir hata oluştu: {e}")

# Kullanım Örneği
# sender_email = "your_email@gmail.com"  # Gönderici e-posta adresi
# sender_password = "your_app_password"  # Uygulama şifresi veya hesap şifresi
# receiver_email = "receiver_email@example.com"  # Alıcı e-posta adresi
# subject = "Python ile Gmail'den E-posta Gönderme"
# body = "Bu bir test e-postasıdır. Python ile Gmail üzerinden gönderildi."

# send_gmail(sender_email, sender_password, receiver_email, subject, body)