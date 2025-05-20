from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from prefences_admin import Ui_MainWindow as prefences_AdminUi


class AdminPreferencesPage(QMainWindow):
    def __init__(self,role ="admin"):  # Parametre ekledik
        super().__init__()
        self.role = role  # role parametresini saklıyoruz
        self.ui = prefences_AdminUi()  # prefences_AdminUi importunu burada kullanıyoruz
        self.ui.setupUi(self)

        # Admin işlemleri için gerekli bağlantılar
        self.ui.pushButton_prefences_admin_applications.clicked.connect(self.on_applications_click)
        self.ui.pushButton_prefences_admin_exit.clicked.connect(self.exit_app)
        self.ui.pushButton__prefences_admin_interviews.clicked.connect(self.on_interviews_click)
        self.ui.pushButton_prefences_admin_main_menu.clicked.connect(self.on_main_menu_click)
        self.ui.pushButton__prefences_admin_mentor_interview.clicked.connect(self.on_mentor_interview_click)
        self.ui.pushButton_i_prefences_admin_menu.clicked.connect(self.on_admin_menu_click)

        print(f"Admin sayfası açıldı. Role: {self.role}")


    def on_applications_click(self):
        from basvurular_python import ApplicationsWindow
        self.applications_window = ApplicationsWindow(role=self.role)
        self.applications_window.show()
        self.close()

    def exit_app(self):
        QApplication.quit()

    def on_interviews_click(self):
        from mulakatlar_python import MulakatlarWindow 
        self.interviews_window = MulakatlarWindow(role="admin")
        self.interviews_window.show()
        self.close()

    def on_main_menu_click(self):
        from input_python import LoginPage
        self.login_window = LoginPage()
        self.login_window.show()
        self.close()


    def on_mentor_interview_click(self):
        from mentor_python import MentorApp  # Dairesel importu fonksiyon içine taşıdık
        self.mentor_window = MentorApp(role=self.role)
        self.mentor_window.show()  # Mentor sayfasını gösteriyoruz
        self.close()


    def on_admin_menu_click(self):
        print("Admin Menu button clicked")
        from admin_python import AdminPage  # Dairesel importu fonksiyon içine taşıdık
        self.admin_window = AdminPage(role="admin")
        self.admin_window.show()  # admin sayfasını gösteriyoruz
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminPreferencesPage()
    window.show()
    sys.exit(app.exec())