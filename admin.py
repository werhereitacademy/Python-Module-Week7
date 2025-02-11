from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from backend.windows_manager import WindowManager
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import backend.style as style
from backend.readfile import read

class Ui_MainWindow(object):
    def __init__(self, role=None):
        self.role = role
    def setupUi(self, MainWindow):
        self.main_window = MainWindow 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 400)
        MainWindow.setWindowFlags (QtCore.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute (QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 400))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 400))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1100, 400))
        self.centralwidget.setMaximumSize(QtCore.QSize(1100, 400))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(1100, 370))
        self.frame.setMaximumSize(QtCore.QSize(1100, 370))
        self.frame.setStyleSheet("background-color:rgb(171, 186, 124,0)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 70, 203, 271))
        self.frame_3.setAcceptDrops(False)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtone1event = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButtone1event.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButtone1event.setObjectName("pushButtone1event")
        self.verticalLayout.addWidget(self.pushButtone1event)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_2sendmail = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_2sendmail.setStyleSheet( style.STYLES["QPushButton"])
        self.pushButton_2sendmail.setObjectName("pushButton_2sendmail")
        self.verticalLayout.addWidget(self.pushButton_2sendmail)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_4returnmenu = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_4returnmenu.setStyleSheet( style.STYLES["QPushButton"])
        self.pushButton_4returnmenu.setObjectName("pushButton_4returnmenu")
        self.verticalLayout.addWidget(self.pushButton_4returnmenu)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_3exit = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_3exit.setStyleSheet( style.STYLES["QPushButton"])
        self.pushButton_3exit.setObjectName("pushButton_3exit")
        self.verticalLayout.addWidget(self.pushButton_3exit)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(220, 80, 851, 269))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDisabled(True)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.setColumnWidth(0, 200)  
        self.tableWidget.setColumnWidth(1, 140)  
        self.tableWidget.setColumnWidth(2, 245)  
        self.tableWidget.setColumnWidth(3, 245) 
        self.label1adminmenu = QtWidgets.QLabel(parent=self.frame)
        self.label1adminmenu.setGeometry(QtCore.QRect(500, 10, 401, 51))
        self.label1adminmenu.setStyleSheet(style.STYLES["QLabel_Title"] )
        self.label1adminmenu.setObjectName("label1adminmenu")
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label = QtWidgets.QLabel(parent=self.frame)  # QLabel nesnesi oluştur
        self.label.setGeometry(QtCore.QRect(0, 0, 1100, 370))  # QLabel’in boyutunu ayarla
        self.label.setPixmap(QtGui.QPixmap("images/cloud_2.jpg"))
        self.label.setScaledContents(True)  # Resmin QLabel içine tam sığmasını sağlar
        self.label.lower()  
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButtone1event.clicked.connect(self.SetupTable)
        self.pushButton_4returnmenu.clicked.connect(self.go_to)
        self.pushButton_3exit.clicked.connect(self.exitApplication)
        self.pushButton_2sendmail.clicked.connect(self.send_emails)


        self.dragPos = None
        MainWindow.mousePressEvent = self.mousePressEvent
        MainWindow.mouseMoveEvent = self.mouseMoveEvent
        MainWindow.mouseReleaseEvent = self.mouseReleaseEvent


    def go_to(self):
        
        
        if hasattr(self, "main_window"):  # Eğer main_window tanımlıysa
            self.main_window.close() 
            self.windows_manager= WindowManager()  
        
        self.windows_manager.open_window("pam",role=self.role)
        

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
        self.pushButtone1event.setText(_translate("MainWindow", "EVENT REGISTRATION"))
        self.pushButton_2sendmail.setText(_translate("MainWindow", "SEND E-MAIL"))
        self.pushButton_4returnmenu.setText(_translate("MainWindow", "RETURN TO ADMIN \n"
" PREFERENCE MENU"))
        self.pushButton_3exit.setText(_translate("MainWindow", "EXIT"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Event Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Start Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Participant Email"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Organizer Email"))
        self.label1adminmenu.setText(_translate("MainWindow", "ADMIN MENU"))

    def SetupTable (self):
        file_path = "Evenement.xlsx" 
        df=read(file_path)
        if df is None or df.empty:
            QtWidgets.QMessageBox.warning(None, "Warning", "No events found or the file is empty!")
            self.tableWidget.setRowCount(0)  # Tabloyu temizle
            return
        self.tableWidget.setRowCount(len(df))  
        self.tableWidget.setColumnCount(len(df.columns)) 
        self.tableWidget.setHorizontalHeaderLabels(df.columns)  

        for row in range(len(df)):
                for col in range(len(df.columns)):
                        item = QtWidgets.QTableWidgetItem(str(df.iloc[row, col]))
                        self.tableWidget.setItem(row, col, item)
        QtWidgets.QMessageBox.information(None, "Succesful", "Evenemets loaded successfully!")
        
            
                

        

    def send_emails(self):
        self.sender_email = "naa710454@gmail.com"
        self.sender_password = "wpnh pxcx cuhh mcyf "  # Use an app password if using Gmail
        self.subject = "Event Reminder"
        tablewidget = self.tableWidget  
        
        if not isinstance(tablewidget, QtWidgets.QTableWidget):
                QMessageBox.critical(None, "Error", "Table widget is not valid.")
                return
       
        recipient_emails = []
        for row in range(tablewidget.rowCount()):
                participant_email = tablewidget.item(row, 2)  
                organiser_email = tablewidget.item(row, 3)  
                if participant_email and participant_email.text():
                        recipient_emails.append(participant_email.text())
                if organiser_email and organiser_email.text():
                        recipient_emails.append(organiser_email.text())
        
        recipient_emails = list(set(recipient_emails))    
        body = "Dear Participant,\n\nThis is a reminder for your upcoming event.\n\nBest regards,\nEvent Organizer"

        try:
                # Set up SMTP server
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(self.sender_email, self.sender_password)

                for recipient in recipient_emails:
                        msg = MIMEMultipart()
                        msg["From"] = self.sender_email
                        msg["To"] = recipient
                        msg["Subject"] = self.subject
                        msg.attach(MIMEText(body, "plain"))

                        server.sendmail(self.sender_email, recipient, msg.as_string())

                server.quit()
                QMessageBox.information(None, "Success", "Emails sent successfully!")

        except Exception as e:
                QMessageBox.critical(None, "Error", f"Email sending failed:\n{str(e)}")

    

    def exitApplication(self):
        QtWidgets.QApplication.quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
