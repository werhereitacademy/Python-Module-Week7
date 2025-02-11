
from PyQt6 import QtCore, QtGui, QtWidgets
import backend.style as style 
from backend.login_backend import authenticate_user


from backend.windows_manager import WindowManager

class UI_login(object):
    def __init__(self, role=None):
        self.role = role
    def setupUi(self, MainWindow):
        self.main_window = MainWindow 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 770)
        MainWindow.setMinimumSize(QtCore.QSize(650, 500))
        MainWindow.setMaximumSize(QtCore.QSize(650, 500))
        
        MainWindow.setStyleSheet(style.STYLES["QMainWindow"])
       
        MainWindow.setWindowFlags (QtCore.Qt.WindowType.FramelessWindowHint)
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 1000, 1000))
        self.frame.setObjectName("frame")

        # Butonları oluştur ve stil ver
        self.pushButton1login = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton1login.setGeometry(QtCore.QRect(310, 370, 121, 31))
        self.pushButton1login.setStyleSheet(style.STYLES["QPushButton"])  # Butona stil uygula
        self.pushButton1login.setObjectName("pushButton1login")

        self.pushButton_2exit = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2exit.setGeometry(QtCore.QRect(310, 440, 121, 31))
        self.pushButton_2exit.setStyleSheet(style.STYLES["QPushButton"])  # Aynı stil
        self.pushButton_2exit.setObjectName("pushButton_2exit")

        # Kullanıcı adı ve şifre giriş alanları
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(260, 190, 211, 41))
        self.lineEdit.setStyleSheet(style.STYLES["QLineEdit"])  # Stil uygula
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 280, 211, 41))
        self.lineEdit_2.setStyleSheet(style.STYLES["QLineEdit"])  # Stil uygula
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        
        self.label1username = QtWidgets.QLabel(parent=self.frame)
        self.label1username.setGeometry(QtCore.QRect(110, 190, 121, 31))
        self.label1username.setStyleSheet(style.STYLES["QLabel"])  # Stil uygula
        self.label1username.setObjectName("label1username")

        self.label_2password = QtWidgets.QLabel(parent=self.frame)
        self.label_2password.setGeometry(QtCore.QRect(110, 280, 131, 31))
        self.label_2password.setStyleSheet(style.STYLES["QLabel"])  # Stil uygula
        self.label_2password.setObjectName("label_2password")
        
        self.label_3crm = QtWidgets.QLabel(parent=self.frame)
        self.label_3crm.setGeometry(QtCore.QRect(320, 80, 141, 41))
        self.label_3crm.setStyleSheet(style.STYLES["QLabel_Title"])  # Stil uygula
        self.label_3crm.setObjectName("label_3crm")

        MainWindow.setCentralWidget(self.centralwidget)
        

        self.error_message = QtWidgets.QLabel(parent=self.frame)
        self.error_message.setGeometry(QtCore.QRect(260, 320, 211, 30))
        self.error_message.setStyleSheet("color: red;")  # Hata mesajını kırmızı yap
        self.error_message.setObjectName("error_message")
        self.error_message.setText("")


        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 1000 , 1000))
        self.label.setText("")
        self.label.setPixmap(
            QtGui.QPixmap(
                "images/cloud_1.jpg"
            )
        )
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # Z-order düzenlemesi
        self.label.lower()


        # Butona tıklama olayı bağlandı
        self.pushButton1login.clicked.connect(self.print_input_values)
        self.pushButton_2exit.clicked.connect(MainWindow.close)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Kapatma butonu (X)
        self.close_button = QtWidgets.QPushButton(parent=self.frame)
        self.close_button.setGeometry(QtCore.QRect(620, 20, 30, 30))  # Sağ üst köşeye koy
        self.close_button.setText("✖")  
        self.close_button.setStyleSheet(style.STYLES["QPushButton"])
        self.close_button.setObjectName("close_button")
        self.close_button.clicked.connect(MainWindow.close)
        # Mouse eventler için değişkenler
        self.dragPos = None
        MainWindow.mousePressEvent = self.mousePressEvent
        MainWindow.mouseMoveEvent = self.mouseMoveEvent
        MainWindow.mouseReleaseEvent = self.mouseReleaseEvent

    def mousePressEvent(self, event):
        """Pencereyi sürüklemek için basıldığında çağrılan fonksiyon"""
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        """Mouse hareket ettikçe pencereyi taşıyan fonksiyon"""
        if self.dragPos is not None:
            self.main_window.move(self.main_window.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        """Mouse düğmesi bırakıldığında sürüklemeyi durduran fonksiyon"""
        self.dragPos = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1login.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton_2exit.setText(_translate("MainWindow", "EXIT"))
        self.label1username.setText(_translate("MainWindow", "USERNAME"))
        self.label_2password.setText(_translate("MainWindow", "PASSWORD"))
        self.label_3crm.setText(_translate("MainWindow", "CRM"))

    def print_input_values(self):  # <-- Eklendi
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        
        is_authenticated, role =  authenticate_user(username, password)
        
        if is_authenticated==False and role==None:
            self.error_message.setText("Check the username or password")
        elif is_authenticated==None and role==None:
            self.error_message.setText("Database can not be loaded")
        else:
            
            print(f"Role is {role}")
            self.error_message.setText("") 
            if hasattr(self, "main_window"):  # Eğer main_window tanımlıysa
                self.main_window.close()  # Hata mesajını temizle
            self.window_manager = WindowManager()
            
                       
            # Login sayfasını kapat ve Deneme sayfasını aç
              # MainWindow'u kapat
            self.window_manager.open_window("Pam",role=role)

            

  

 # "Enter" tuşuna basıldığında login butonunu tetiklemek için
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.print_input_values() 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

