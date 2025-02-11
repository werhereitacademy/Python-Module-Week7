import backend.style as style 


from PyQt6 import QtCore, QtGui, QtWidgets
from backend.windows_manager import WindowManager

class UI_Pam(object):
    def __init__(self, role="user"):
        self.role = role
    def setupUi(self, MainWindow):
        self.main_window = MainWindow 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setMinimumSize(QtCore.QSize(700, 600))
        MainWindow.setMaximumSize(QtCore.QSize(700, 600))
        MainWindow.setStyleSheet("background-color:rgb(255, 255, 255)")

        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.frame.setStyleSheet(style.STYLES["Qpam"])
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.pushButton1applications = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton1applications.setGeometry(QtCore.QRect(100, 170, 171, 51))
        self.pushButton1applications.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton1applications.setObjectName("pushButton1applications")
        self.pushButton_2mentormeeting = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2mentormeeting.setGeometry(QtCore.QRect(410, 170, 181, 51))
        self.pushButton_2mentormeeting.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_2mentormeeting.setObjectName("pushButton_2mentormeeting")
        self.pushButton_5returmainmenu = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_5returmainmenu.setGeometry(QtCore.QRect(410, 510, 191, 51))
        self.pushButton_5returmainmenu.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_5returmainmenu.setObjectName("pushButton_5returmainmenu")
        self.pushButton_3interviews = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_3interviews.setGeometry(QtCore.QRect(250, 290, 191, 51))
        self.pushButton_3interviews.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_3interviews.setObjectName("pushButton_3interviews")
        self.pushButton_4exit = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_4exit.setGeometry(QtCore.QRect(100, 510, 171, 51))
        self.pushButton_4exit.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_4exit.setObjectName("pushButton_4exit")

        
        self.labelbaslikpreadmin = QtWidgets.QLabel(parent=self.frame)
        self.labelbaslikpreadmin.setGeometry(QtCore.QRect(160, 30, 361, 51))
        self.labelbaslikpreadmin.setStyleSheet(style.STYLES["QLabel"])
        self.labelbaslikpreadmin.setObjectName("labelbaslikpreadmin")

        
        

        if self.role=="admin":
            self.pushButton_6adminmenu = QtWidgets.QPushButton(parent=self.frame)
            self.pushButton_6adminmenu.setGeometry(QtCore.QRect(250, 390, 191, 51))
            self.pushButton_6adminmenu.setStyleSheet(style.STYLES["QPushButton"])
            self.pushButton_6adminmenu.setObjectName("pushButton_6adminmenu")
            self.pushButton_6adminmenu.clicked.connect(lambda: self.go_to("admin"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 900 , 700))
        self.label.setText("")
        self.label.setPixmap(
            QtGui.QPixmap(
                "images/cloud_3.jpg"
            )
        )
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.lower()
        #When The buttons are clicked
        self.pushButton_5returmainmenu.clicked.connect(lambda: self.go_to("login"))
        
        self.pushButton_4exit.clicked.connect(MainWindow.close)
        self.pushButton_3interviews.clicked.connect(lambda: self.go_to("interviews"))
        self.pushButton_2mentormeeting.clicked.connect(lambda: self.go_to("mentor"))
        self.pushButton1applications.clicked.connect(lambda: self.go_to("applications"))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setWindowFlags (QtCore.Qt.WindowType.FramelessWindowHint)
        self.dragPos = None
        MainWindow.mousePressEvent = self.mousePressEvent
        MainWindow.mouseMoveEvent = self.mouseMoveEvent
        MainWindow.mouseReleaseEvent = self.mouseReleaseEvent
    def go_to(self,page):
        print(page)
        if hasattr(self, "main_window"):  # Eğer main_window tanımlıysa
            self.main_window.close() 
        
        self.windows_manager= WindowManager()
        self.windows_manager.open_window(page,self.role)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1applications.setText(_translate("MainWindow", "APPLICATIONS"))
        self.pushButton_2mentormeeting.setText(_translate("MainWindow", "MENTOR MEETING"))
        self.pushButton_5returmainmenu.setText(_translate("MainWindow", "RETURN MAIN MENU"))
        self.pushButton_3interviews.setText(_translate("MainWindow", "INTERVIEWS"))
        self.pushButton_4exit.setText(_translate("MainWindow", "EXIT"))
        
        self.labelbaslikpreadmin.setText(_translate("MainWindow", f"PREFERENCE {self.role.upper()} MENU"))
        if self.role=="admin":
            self.pushButton_6adminmenu.setText(_translate("MainWindow", "ADMIN MENU"))
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_Pam()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
