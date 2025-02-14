from PyQt6 import QtWidgets, uic,QtCore, QtGui
import pandas as pd
import sys
from PyQt6.QtWidgets import QTableWidgetItem,QHeaderView,QApplication
import backend.style as style
from backend.windows_manager import WindowManager
from backend.readfile import read
class Ui_Application_Menu(object):
    def __init__(self, role="admin"):
        self.role = role
        self.df=None
        
    def setupUi(self, MainWindow):
        self.load()
        self.main_window = MainWindow 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1150, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1150, 600))
        screen = QApplication.primaryScreen().geometry() 
        
        x = (screen.width() - 1150) // 2  
        y = (screen.height() - 750) // 2  

        MainWindow.setGeometry(x, y, 1150, 750)

        MainWindow.setWindowFlags (QtCore.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute (QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-40, -10, 1150, 600))
        self.frame.setStyleSheet("background-color: rgb(202, 224, 188,0)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.pushButton1search = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton1search.setGeometry(QtCore.QRect(100, 110, 181, 41))
        self.pushButton1search.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton1search.setObjectName("pushButton1search")
        self.pushButton_2allapplications = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2allapplications.setGeometry(QtCore.QRect(100, 180, 249, 41))
        self.pushButton_2allapplications.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_2allapplications.setObjectName("pushButton_2allapplications")
        self.pushButton_3vitcheck = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_3vitcheck.setGeometry(QtCore.QRect(880, 250, 249, 41))
        self.pushButton_3vitcheck.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_3vitcheck.setObjectName("pushButton_3vitcheck")
        self.pushButton_4definedmentor = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_4definedmentor.setGeometry(QtCore.QRect(360, 180, 249, 41))
        self.pushButton_4definedmentor.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_4definedmentor.setObjectName("pushButton_4definedmentor")
        self.pushButton_5endefined = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_5endefined.setGeometry(QtCore.QRect(360, 250, 249, 41))
        self.pushButton_5endefined.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_5endefined.setObjectName("pushButton_5endefined")
        self.pushButton_6returnpremenu = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_6returnpremenu.setGeometry(QtCore.QRect(100, 250, 249, 41))
        self.pushButton_6returnpremenu.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_6returnpremenu.setObjectName("pushButton_6returnpremenu")
        self.pushButton_7duplicatereg = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_7duplicatereg.setGeometry(QtCore.QRect(620, 250, 249, 41))
        self.pushButton_7duplicatereg.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_7duplicatereg.setObjectName("pushButton_7duplicatereg")
        self.lineEdit1aramabosluk = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit1aramabosluk.setGeometry(QtCore.QRect(340, 110, 771, 41))
        self.lineEdit1aramabosluk.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit1aramabosluk.setStyleSheet(style.STYLES["QLineEdit"])
        self.lineEdit1aramabosluk.setObjectName("lineEdit1aramabosluk")
        self.label2applications = QtWidgets.QLabel(parent=self.frame)
        self.label2applications.setGeometry(QtCore.QRect(350, 30, 471, 41))
        self.label2applications.setStyleSheet(style.STYLES["QLabel"])
        self.label2applications.setObjectName("label2applications")
        self.pushButton_8differentreg = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_8differentreg.setGeometry(QtCore.QRect(620, 180, 249, 41))
        self.pushButton_8differentreg.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_8differentreg.setObjectName("pushButton_8differentreg")
        self.pushButton_9appfilter = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_9appfilter.setGeometry(QtCore.QRect(880, 180, 249, 41))
        self.pushButton_9appfilter.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButton_9appfilter.setObjectName("pushButton_9appfilter")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget_2.setGeometry(QtCore.QRect(100, 320, 1010, 250))
        self.tableWidget_2.setStyleSheet("background-color: rgba(255, 255, 255)")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(129)

        self.tableWidget_2.setColumnWidth(0, 110) 
        self.tableWidget_2.setColumnWidth(1, 135)
        self.tableWidget_2.setColumnWidth(2, 200)
        self.tableWidget_2.setColumnWidth(3, 120)
        self.tableWidget_2.setColumnWidth(4, 100)
        self.tableWidget_2.setColumnWidth(5, 120)
        self.tableWidget_2.setColumnWidth(6, 223)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)  # Değiştirilemez



        self.label = QtWidgets.QLabel(parent=self.frame) 
        self.label.setGeometry(QtCore.QRect(0, 0, 1600, 1000))  
        self.label.setPixmap(QtGui.QPixmap("images/cloud_4.jpg"))
        self.label.setScaledContents(True)  
        self.label.lower() 
        MainWindow.setCentralWidget(self.centralwidget)
       

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.mousePressEvent = self.mousePressEvent
        MainWindow.mouseMoveEvent = self.mouseMoveEvent
        MainWindow.mouseReleaseEvent = self.mouseReleaseEvent
        self.pushButton1search.clicked.connect(self.search_names)
        self.pushButton_2allapplications.clicked.connect(self.load_selected_data) 
        self.pushButton_4definedmentor.clicked.connect(self.defined_mentor)
        self.pushButton_5endefined.clicked.connect(self.undefined_mentor)
        self.pushButton_3vitcheck.clicked.connect(self.vit_control)
        self.pushButton_8differentreg.clicked.connect(self.different_control)
        self.pushButton_7duplicatereg.clicked.connect(self.duplicate_control)
        self.pushButton_9appfilter.clicked.connect(self.app_filter)
        self.pushButton_6returnpremenu.clicked.connect(self.go_to)
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
        self.pushButton_2allapplications.setText(_translate("MainWindow", "ALL APPLICATIONS"))
        self.pushButton_3vitcheck.setText(_translate("MainWindow", "PREVIOUS VIT CHECK"))
        self.pushButton_4definedmentor.setText(_translate("MainWindow", "DEFINED MENTOR MEETING"))
        self.pushButton_5endefined.setText(_translate("MainWindow", "UNDEFINED MENTOR MEETING"))
        self.pushButton_6returnpremenu.setText(_translate("MainWindow", f"RETURN TO {self.role.upper()}\n PREFERENCE MENU"))
        self.pushButton_7duplicatereg.setText(_translate("MainWindow", "DUPLICATE REGISTRATION "))
        self.lineEdit1aramabosluk.setPlaceholderText(_translate("MainWindow", "Enter the text you want to search for here"))
        self.label2applications.setText(_translate("MainWindow", "               APPLICATIONS"))
        self.pushButton_8differentreg.setText(_translate("MainWindow", "DIFFERENT REGISTRATION"))
        self.pushButton_9appfilter.setText(_translate("MainWindow", "APPLICATION FILTERING"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DATE"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "FULL NAME"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "E-MAIL"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PHONE NUMBER"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "POSTAL CODE"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "PROVINCE"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", " CURRENT STATUS"))

        self.tableWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)   
    def load(self):
        
        self.df = read("Basvurular.xlsx")
        if self.df is None or self.df.empty:
            print("Veri seti yüklenemedi veya boş.")  
            self.df = pd.DataFrame()  # Boş DataFrame ile devam et
        
    def go_to(self):
        
        
        if hasattr(self, "main_window"): 
            self.main_window.close() 
            self.windows_manager= WindowManager()  
        
        self.windows_manager.open_window("pam",role=self.role)
        

    def app_filter(self):
        
        filtered_df = self.df.drop_duplicates(subset=["Adınız Soyadınız", "Mail adresiniz"], keep="first")
        
        self.populate_table(filtered_df)

    def duplicate_control(self):


        filtered_df = self.df[self.df.duplicated(subset=["Adınız Soyadınız", "Mail adresiniz"], keep=False)]

        self.populate_table(filtered_df)


    def different_control(self):
       

        filtered_df = self.df[self.df["Daha once basvurdunuz mu?"].str.contains("Hayır", na=False)]

        self.populate_table(filtered_df)
        
    def vit_control(self):
        
        filtered_df = self.df[self.df["Daha once basvurdunuz mu?"].str.contains("Evet", na=False)]

        self.populate_table(filtered_df) 

    def undefined_mentor(self):
    

        mentor_atanmadi=self.df[ self.df["Mentor gorusmesi"].str.strip() == "ATANMADI"].reset_index(drop=True)
        mentor_atanmadi = mentor_atanmadi.drop_duplicates(subset=["Adınız Soyadınız", "Mail adresiniz"], keep="first")
        mentor_atanmadi = mentor_atanmadi.iloc[:, :7]


        self.populate_table(mentor_atanmadi)

    def defined_mentor(self):
        

        if "Mentor gorusmesi" not in self.df.columns:
            self.tableWidget_2.setRowCount(0)
            return
            
        
        mentor_ok = self.df[ self.df["Mentor gorusmesi"].str.strip() == "OK"].reset_index(drop=True)
        
        mentor_ok = mentor_ok.drop_duplicates(subset=["Adınız Soyadınız", "Mail adresiniz"], keep="first")
        
        if mentor_ok.empty:
            self.tableWidget_2.setRowCount(0)
            return
        self.populate_table(mentor_ok)

    def search_names(self):
        """Girilen harflerle BAŞLAYAN isimleri bul ve QTableWidget'te göster."""
        search_text = self.lineEdit1aramabosluk.text().strip().lower()

        if not search_text:  
            self.tableWidget_2.setRowCount(0) 
            return

        df = pd.read_excel("Files/Basvurular.xlsx", dtype=str)

       
        if "Adınız Soyadınız" not in df.columns:
            self.tableWidget_2.setRowCount(0)
            return  

        #  Girilen harflerle BAŞLAYAN isimleri filtrele
        matches = df[df["Adınız Soyadınız"].str.lower().str.startswith(search_text)]


        # Eğer sonuç yoksa tabloyu temizle
        if matches.empty:
            self.tableWidget_2.setRowCount(0)
            return
        
        self.populate_table(matches)

    def load_selected_data(self):

        """file_path = "Files/Basvurular.xlsx" 
        df = pd.read_excel(file_path) """
        
        self.populate_table(self.df)

    def populate_table(self, df):
        df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0]).dt.date 

        df = df.iloc[:, :7] 
        self.tableWidget_2.setRowCount(df.shape[0])
        self.tableWidget_2.setColumnCount(df.shape[1])
        
        # DataFrame'deki verileri tabloya ekle
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QtWidgets.QTableWidgetItem(str(df.iat[row, col]))
                self.tableWidget_2.setItem(row, col, item)
                # ToolTip ekleme
                self.tableWidget_2.item(row, col).setToolTip(str(df.iat[row, col]))  # Tooltip gösterme


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Application_Menu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
