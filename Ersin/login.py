import os
from PyQt6 import QtCore, QtGui, QtWidgets
from preference_adminmenu import Ui_MainWindow as AdminMenuWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # Merkez widget oluştur
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # QLabel kullanarak arka plan resmi
        self.background_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 800, 600))

        # Dinamik yol ile resim ekleme
        image_path = os.path.join(os.path.dirname(__file__), 'images', 'login.jpg')
        
        # Resmi QLabel'a ekle
        pixmap = QtGui.QPixmap(image_path)
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)  # Resmin QLabel boyutlarına göre ölçeklenmesi
        self.background_label.lower()  # Resmi arka plana yerleştir

        # CRM Project başlığı
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 120, 291, 61))
        self.label.setObjectName("label")
        
        # Kullanıcı adı girişi
        self.Username = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(520, 230, 171, 31))
        self.Username.setObjectName("Username")
        
        # Şifre girişi
        self.Password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(520, 270, 171, 31))
        self.Password.setObjectName("Password")
        self.Password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Şifre gizleme
        
        # Giriş butonu
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 320, 171, 31))
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Login butonuna tıklama olayı
        self.pushButton.clicked.connect(self.open_admin_menu)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:30pt; font-weight:1200; color:#ffffff;\">CRM PROJECT</span></p></body></html>"))
        self.Username.setPlaceholderText(_translate("MainWindow", "UserName"))
        self.Password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))

    def open_admin_menu(self):
        # Admin menüyü açmak için
        self.window = QtWidgets.QMainWindow()  # Yeni bir QMainWindow oluşturuluyor
        self.ui = AdminMenuWindow()  # preference_admin_menu dosyasındaki Ui_MainWindow sınıfı kullanılıyor
        self.ui.setupUi(self.window)  # Arayüz setup ediliyor
        self.window.show()  # Yeni pencere gösteriliyor

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
