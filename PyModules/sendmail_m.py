import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_gmail(recipient_email , subject, body):
    """
    Gmail üzerinden e-posta gönderen fonksiyon.

    :param sender_email: Gönderenin Gmail adresi (örn: 'your_email@gmail.com')
    :param sender_password: Gönderenin Gmail uygulama şifresi veya hesap şifresi
    :param recipient_email: Alıcının e-posta adresi (örn: 'recipient@example.com')
    :param subject: E-postanın konusu
    :param body: E-postanın içeriği
    :return: Başarılıysa True, hata oluşursa False döner.
    """

    sender_email=""
    sender_password=""
    
    try:
        # E-posta oluşturma
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # E-posta gövdesi
        msg.attach(MIMEText(body, 'plain'))

        # SMTP sunucusuna bağlanma ve e-posta gönderme
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Güvenli bağlantı kur
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print('E-posta başarıyla gönderildi!')
        return True
    except Exception as e:
        print(f'E-posta gönderilirken bir hata oluştu: {e}')
        return False

# # Örnek kullanım
# sender_email = 'your_email@gmail.com'  # Gönderenin Gmail adresi
# sender_password = 'your_app_password'  # Gönderenin uygulama şifresi
# recipient_email = 'recipient@example.com'  # Alıcının e-posta adresi
# subject = 'Python ile Gmail Gönderme'
# body = 'Bu bir test e-postasıdır.'

# # Fonksiyonu çağır
# send_gmail(sender_email, sender_password, recipient_email, subject, body)