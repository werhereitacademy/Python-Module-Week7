
import sys
import json
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QInputDialog, QLineEdit
from googleapiclient.discovery import build
from google.oauth2 import service_account
from admin import Ui_MainWindow_admin  # admin.py'den sadece UI sınıfını import ediyoruz



class AdminPage(QtWidgets.QMainWindow): 
    def __init__(self,role):
        super().__init__()
        self.ui = Ui_MainWindow_admin()  # Önceden dönüştürülmüş olan UI sınıfını kullanıyoruz
        self.ui.setupUi(self)  # UI öğelerini yüklemek için
        self.event_data = [] 
        self.role = role

        self.ui.pushButton_EVENT_CONTROL.clicked.connect(self.etkinlik_kaydi)
        self.ui.pushButton_SEND_MAIL.clicked.connect(self.mail_gonder)
        self.ui.pushButton_PREFENCES_ADMIN.clicked.connect(self.go_back)
        self.ui.pushButton_EXIT.clicked.connect(self.exit)

    def etkinlik_kaydi(self):
        """Google Calendar'dan etkinlikleri al"""
        SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
        SERVICE_ACCOUNT_FILE = 'snm.json'  # Service Account JSON dosyanızın yolu
        
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # Google Calendar API'ye bağlanma
        service = build('calendar', 'v3', credentials=credentials)

        # Etkinlikleri alma (Google Calendar API'den)
        events_result = service.events().list(
            calendarId='primary', timeMin='2025-02-17T00:00:00Z',  # Başlangıç tarihini belirleyin
            maxResults=10, singleEvents=True, orderBy='startTime').execute()
        
        events = events_result.get('items', [])

        if not events:
            print('Etkinlik bulunamadı.')
        else:
            # Etkinlikleri ekrana yazdırma
            self.event_data = []
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                self.event_data.append(f"{event['summary']} - {start}")
            
            # Etkinlikleri ekranda göstermek için uygun bir alan kullanabilirsiniz
            self.ui.textBrowser.setText("\n".join(self.event_data))  # Örneğin, TextBrowser kullanarak gösterim
            print("Etkinlikler listelendi.")

    def mail_gonder(self):
        """Etkinlikte kayıtlı e-mail adreslerine mail gönder"""
        SCOPES = ['https://www.googleapis.com/auth/gmail.send']
        SERVICE_ACCOUNT_FILE = 'snm.json'  # Service Account JSON dosyanızın yolu

        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # Gmail API'ye bağlanma
        service = build('gmail', 'v1', credentials=credentials)

        # Mail gönderilecek kullanıcılar
        recipient_emails = self.get_event_emails()

        for email in recipient_emails:
            message = self.create_message("your_email@gmail.com", email, "Etkinlik Hatırlatması", "Etkinliğiniz yaklaşıyor!")
            self.send_message(service, "me", message)

    def get_event_emails(self):
        """Etkinliklerden kayıtlı e-mail adreslerini al"""
        emails = []
        for event in self.event_data:
            if "@" in event:
                emails.append(event)  # Bu örnekte e-postaları etkinlik verisinden alıyoruz
        return emails

    def create_message(self, sender, to, subject, body):
        """Mail mesajı oluşturma"""
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        message = MIMEMultipart()
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject

        msg = MIMEText(body)
        message.attach(msg)
        return {'raw': message.as_string()}

    def send_message(self, service, sender, message):
        """Maili gönderme"""
        try:
            send_message = service.users().messages().send(userId=sender, body=message).execute()
            print('Message Id: %s' % send_message['id'])
        except Exception as error:
            print(f'Bir hata oluştu: {error}')



    # Geri Dön Butonu İşlevi
    def go_back(self):
        print(f"Geri dönme işlemi başlatıldı. Rol: {self.role}")  # Debugging
        self.close()

        if self.role == "admin":
            print("Admin paneline yönlendiriliyor...")  # Debugging
            import prefences_admin_python
            self.admin_preferences = prefences_admin_python.AdminPreferencesPage()
            self.admin_preferences.show()
            print("Admin sayfasına geri dönüldü.")  # Debugging
        else:
            print("Kullanıcı paneline yönlendiriliyor...")  # Debugging
            import prefences_python
            self.user_preferences = prefences_python.PreferencesPage()
            self.user_preferences.show()
            print("Kullanıcı sayfasına geri dönüldü.")  # Debugging



    # cikis İşlevi
    def exit(self):
        QtWidgets.QApplication.quit()