from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from prefences import Ui_MainWindow as prefences_Ui # preferences.py içindeki sınıfı çağır

class PreferencesPage(QMainWindow):
    def __init__(self,role ="user"):
        super().__init__()
        self.role = role
        self.ui = prefences_Ui()  # Arayüz sınıfını başlat
        self.ui.setupUi(self)  # Arayüzü yükle

        # Butonları bağlama
        #self.ui.pushButton_prefences_exit.clicked.connect(self.exit_app)


        self.ui.pushButton_applications.clicked.connect(self.on_applications_user_click)
        self.ui.pushButton_prefences_exit.clicked.connect(self.exit_app)
        self.ui.pushButton_interviews.clicked.connect(self.on_interviews_user_click)
        self.ui.pushButton_prefences_main_menu.clicked.connect(self.on_main_menu__user_click)
        self.ui.pushButton_mentor_interview.clicked.connect(self.on_mentor_interview_user_click)
        
        
    def on_applications_user_click(self):
        from basvurular_python import ApplicationsWindow
        self.applications_window = ApplicationsWindow(role=self.role)
        self.applications_window.show()
        self.close()

  

    def on_interviews_user_click(self):
        from mulakatlar_python import MulakatlarWindow 
        self.interviews_window = MulakatlarWindow(role=self.role)
        self.interviews_window.show()
        self.close()


    def on_main_menu__user_click(self):
        from input_python import LoginPage
        self.login_window = LoginPage()
        self.login_window.show()
        self.close()


    def on_mentor_interview_user_click(self):
        from mentor_python import MentorApp  # Dairesel importu fonksiyon içine taşıdık
        self.mentor_window = MentorApp(role=self.role)
        self.mentor_window.show()  # Mentor sayfasını gösteriyoruz
        self.close()



    def exit_app(self):
        self.close()  # Pencereyi kapat

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PreferencesPage()
    window.show()
    sys.exit(app.exec())

