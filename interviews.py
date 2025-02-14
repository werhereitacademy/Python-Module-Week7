import re
import backend.style as style 
from backend.interview_backed import load_data_to_table
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
from backend.readfile import read
from backend.windows_manager import WindowManager
class UI_Im(object):
    def __init__(self, role="admin"):
        self.role = role
        self.df=None
       
    def setupUi(self, MainWindow):
        w=1600
        h=1000
        self.main_window = MainWindow 
        screen = QApplication.primaryScreen().geometry()  
        x = (screen.width() - 1150) // 2  
        y = (screen.height() - 750) // 2  

        MainWindow.setGeometry(x, y, 1150, 670)  
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1150, 670))
        MainWindow.setMaximumSize(QtCore.QSize(1150, 670))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-90, -150, w, h))
        self.frame.setStyleSheet("background-color:rgb(177, 194, 158,0)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.pushButton1search = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton1search.setGeometry(QtCore.QRect(470, 260, 171, 51))
        self.pushButton1search.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton1search.setObjectName("pushButton1search")
        self.pushButton_2submitted = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2submitted.setGeometry(QtCore.QRect(120, 260, 211, 61))
        self.pushButton_2submitted.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_2submitted.setObjectName("pushButton_2submitted")
        self.lineEditaramabosluk = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEditaramabosluk.setGeometry(QtCore.QRect(670, 260, 461, 51))
        self.lineEditaramabosluk.setStyleSheet(style.STYLES["QLineEdit"])
        self.lineEditaramabosluk.setObjectName("lineEditaramabosluk")
        self.pushButton_3returnmenu = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_3returnmenu.setGeometry(QtCore.QRect(120, 540, 211, 61))
        self.pushButton_3returnmenu.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_3returnmenu.setObjectName("pushButton_3returnmenu")
        self.pushButton_4received = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_4received.setGeometry(QtCore.QRect(120, 390, 211, 61))
        self.pushButton_4received.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_4received.setObjectName("pushButton_4received")
        self.pushButton_5exit = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_5exit.setGeometry(QtCore.QRect(120, 710, 211, 51))
        self.pushButton_5exit.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_5exit.setObjectName("pushButton_5exit")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(470, 390, 660, 371))
        self.tableWidget.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDisabled(True)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(218)
        self.label3interviews = QtWidgets.QLabel(parent=self.frame)
        self.label3interviews.setGeometry(QtCore.QRect(500, 160, 210, 71))
        self.label3interviews.setStyleSheet(style.STYLES["QLabel"])
        self.label3interviews.setObjectName("label3interviews")
        MainWindow.setCentralWidget(self.centralwidget)
       
        self.load()


        self.error_message = QtWidgets.QLabel(parent=self.frame)
        self.error_message.setGeometry(QtCore.QRect(260, 320, 211, 30))
        self.error_message.setStyleSheet("color: red;")  
        self.error_message.setObjectName("error_message")
        self.error_message.setText("") 

        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, w , h))
        self.label.setText("")
        self.label.setPixmap(
            QtGui.QPixmap(
                "images/cloud_3.jpg"
            )
        )
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # Z-order düzenlemesi
        self.label.lower()
        #Çıkış
        self.pushButton_5exit.clicked.connect(MainWindow.close)

        #SubmittedApplications
        self.pushButton_2submitted.clicked.connect(self.submitted)
        
        #ReceivedApplications
        self.pushButton_4received.clicked.connect(self.received)

        
        #ReturnMenu
        self.pushButton_3returnmenu.clicked.connect(self.go_to)

        self.pushButton1search.clicked.connect(self.search)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setWindowFlags (QtCore.Qt.WindowType.FramelessWindowHint)
        self.dragPos = None
        MainWindow.mousePressEvent = self.mousePressEvent
        MainWindow.mouseMoveEvent = self.mouseMoveEvent
        MainWindow.mouseReleaseEvent = self.mouseReleaseEvent
        
    def mousePressEvent(self, event):
       
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        
        if self.dragPos is not None:
            self.main_window.move(self.main_window.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        
        self.dragPos = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1search.setText(_translate("MainWindow", "SEARCH"))
        self.pushButton_2submitted.setText(_translate("MainWindow", "SUBMITTED PROJECTS"))
        self.lineEditaramabosluk.setPlaceholderText(_translate("MainWindow", "Enter the text you want to search for here"))
        self.pushButton_3returnmenu.setText(_translate("MainWindow", f"RETURN TO {self.role.upper()}\n PREFERENCE MENU"))
        self.pushButton_4received.setText(_translate("MainWindow", "RECEIVED PROJECTS"))
        self.pushButton_5exit.setText(_translate("MainWindow", "EXIT"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Full Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Submission Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Delivery Date"))
        self.label3interviews.setText(_translate("MainWindow", "INTERVIEWS"))
    def load(self):
        self.df=read("Mulakatlar.xlsx")
        if self.df is None or self.df.empty:
            print("can not connect database")
        else:
            load_data_to_table(self.tableWidget, self.df) 

    def received(self):
        if self.df is None or self.df.empty:
            self.tableWidget.setRowCount(0)
            QtWidgets.QMessageBox.warning(self.main_window, "Warning", "No received projects available.")
        else:
            load_data_to_table(self.tableWidget, self.df, filter_column=1, filter_na=True) 
        

    def submitted(self):
        if self.df is None or self.df.empty:
            self.tableWidget.setRowCount(0)
            QtWidgets.QMessageBox.warning(self.main_window, "Warning", "No submitted projects available.")
        else:
            load_data_to_table(self.tableWidget, self.df, filter_column=2, filter_na=True)  
     

    def go_to(self):
        
        
        if hasattr(self, "main_window"):  # Eğer main_window tanımlıysa
            self.main_window.close() 
            self.windows_manager= WindowManager()  
        
        self.windows_manager.open_window("pam",role=self.role)
        
        
        

    def search(self):
        search_text = self.lineEditaramabosluk.text().strip()  
        
        if not search_text:  
            self.load()
            return

        if not re.match("^[a-zA-Z]+$", search_text):  
            QtWidgets.QMessageBox.warning(self.main_window, "Warning", "Please enter only letters.")
            return

        
        load_data_to_table(self.tableWidget, df=self.df ,filter_column=0,filter_na=True, search_text=search_text.lower())
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_Im()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
