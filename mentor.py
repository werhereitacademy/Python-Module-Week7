
from PyQt6 import QtCore, QtWidgets
import pandas as pd
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import backend.style as style
from backend.filter_meetings import filter_meetings
from backend.windows_manager import WindowManager

class Ui_MainWindow(object):
    def __init__(self, role="admin"):
        self.role = role
    def setupUi(self, MainWindow):
        self.main_window=MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 799)
        MainWindow.setMinimumSize(QtCore.QSize(1150, 750))
        MainWindow.setMaximumSize(QtCore.QSize(1250, 850))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-90, -80, 1381, 1000))
        self.frame.setStyleSheet("background-color:rgb(255, 230, 169,0)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(-80, -50, 1591, 1051))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/wallpaper.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.labelbaslikmentormeeting = QtWidgets.QLabel(parent=self.frame)
        self.labelbaslikmentormeeting.setGeometry(QtCore.QRect(510, 80, 331, 61))
        self.labelbaslikmentormeeting.setStyleSheet(style.STYLES["QLabel_Title"])
        self.labelbaslikmentormeeting.setObjectName("labelbaslikmentormeeting")
        self.pushButtonsearch = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonsearch.setGeometry(QtCore.QRect(500, 180, 131, 51))
        self.pushButtonsearch.setStyleSheet(style.STYLES["QPushButton"])
        self.pushButtonsearch.setObjectName("pushButtonsearch")
        self.pushButton_2exit = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2exit.setGeometry(QtCore.QRect(500, 270, 131, 51))
        self.pushButton_2exit.setStyleSheet(style.STYLES["QPushButton"])

        self.pushButton_2exit.setObjectName("pushButton_2exit")
        self.pushButton_3allmeetings = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_3allmeetings.setGeometry(QtCore.QRect(160, 180, 268, 51))
        self.pushButton_3allmeetings.setStyleSheet(style.STYLES["QPushButton"])

        self.pushButton_3allmeetings.setObjectName("pushButton_3allmeetings")
        self.pushButton_4returnmenu = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_4returnmenu.setGeometry(QtCore.QRect(160, 270, 268, 51))
        self.pushButton_4returnmenu.setStyleSheet(style.STYLES["QPushButton"])

        self.pushButton_4returnmenu.setObjectName("pushButton_4returnmenu")
        self.lineEditaramabosluk = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEditaramabosluk.setGeometry(QtCore.QRect(700, 180, 441, 51))
        self.lineEditaramabosluk.setStyleSheet(style.STYLES["QLineEdit"])

        self.lineEditaramabosluk.setText("")
        self.lineEditaramabosluk.setReadOnly(False)
        self.lineEditaramabosluk.setClearButtonEnabled(False)
        self.lineEditaramabosluk.setObjectName("lineEditaramabosluk")
        self.comboBox = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox.setGeometry(QtCore.QRect(700, 280, 451, 31))
        self.comboBox.setStyleSheet(style.STYLES["QPushButton"])
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        x = (screen.width() - 1150) // 2  # X (ortalamak için)
        y = (screen.height() - 750) // 2  # Y (ortalamak için)
        MainWindow.setGeometry(x, y, 1150, 750)  # Pencereyi ortala

        # Pencereyi çerçevesiz yap
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(290, 360, 731, 321))
        self.tableWidget.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(54)
        MainWindow.setCentralWidget(self.centralwidget)
        # Buton bağlantılarını ekliyoruz
        self.pushButton_3allmeetings.clicked.connect(self.show_all_meetings)
        self.pushButton_4returnmenu.clicked.connect(self.return_to_menu)
        self.pushButtonsearch.clicked.connect(self.search_meetings)
        self.pushButton_2exit.clicked.connect(self.exit_application)
        self.comboBox.currentIndexChanged.connect(self.filter_data)

        
        self.tableWidget.setEditTriggers(
            QtWidgets.QTableWidget.EditTrigger.NoEditTriggers
        )
        self.tableWidget.setSelectionBehavior(
            QtWidgets.QTableWidget.SelectionBehavior.SelectRows
        )


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        self.labelbaslikmentormeeting.setText(
            _translate("MainWindow", "MENTOR MEETING PAGE")
        )
        self.pushButtonsearch.setText(_translate("MainWindow", "SEARCH"))
        self.pushButton_2exit.setText(_translate("MainWindow", "EXIT"))
        self.pushButton_3allmeetings.setText(_translate("MainWindow", "ALL MEETINGS"))
        self.pushButton_4returnmenu.setText(
            _translate("MainWindow", f"RETURN TO {self.role.upper()}\n PREFERENCE MENU")
        )
        self.lineEditaramabosluk.setPlaceholderText(
            _translate("MainWindow", "Enter the text you want to search for here")
        )
        self.comboBox.setItemText(
            0,
            _translate(
                "MainWindow",
                "It is appropriate to participate in the entire VIT project",
            ),
        )
        self.comboBox.setItemText(
            1,
            _translate(
                "MainWindow",
                "It is appropriate to receive initial IT training within the VIT project and be directed to ITPH",
            ),
        )
        self.comboBox.setItemText(
            2,
            _translate(
                "MainWindow",
                "It is appropriate to receive English training within the VIT project and be directed to ITPH",
            ),
        )
        self.comboBox.setItemText(
            3,
            _translate(
                "MainWindow",
                "It is appropriate to be directly directed to ITPH within the scope of the VIT project",
            ),
        )
        self.comboBox.setItemText(
            4,
            _translate(
                "MainWindow",
                "It is appropriate to be directed to a job through individual coaching",
            ),
        )
        self.comboBox.setItemText(
            5,
            _translate(
                "MainWindow",
                "It would be more appropriate to participate in the next VIT project",
            ),
        )
        self.comboBox.setItemText(
            6, _translate("MainWindow", "Should be directed to another sector")
        )
        self.comboBox.setItemText(7, _translate("MainWindow", "Other"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Meeting Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Period"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Full Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Mentor"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Evaluation"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Current Status"))
    def show_all_meetings(self):
        # Tüm toplantilari TableWidget'ta gösterir
        try:
            # Excel dosyasını oku
            df = pd.read_excel("Files/Mentor.xlsx")

            # Sadece bu sütunları al (Meeting Date, Period, Full Name, Mentor, Evaluation, Language Level)
            selected_columns = [
                "Meeting Date",
                "Period",
                "Full Name",
                "Mentor",
                "Evaluation",
                "Current Status",
            ]
            df_selected = df[selected_columns]

            # Duplicate olanları filtrele
            df_selected = df_selected.drop_duplicates(
                subset=["Full Name"], keep="first"
            )  # 'Full Name' sütunu duplicateleri kaldır

            # TableWidget'ı temizle
            self.tableWidget.setRowCount(0)

            # Başlıkları (header) ayarla
            headers = df_selected.columns.tolist()  # Seçilen sütun adlarını al
            self.tableWidget.setColumnCount(
                len(headers)
            )  # Sütun sayısını başlık sayısına göre ayarla
            self.tableWidget.setHorizontalHeaderLabels(headers)  # Başlıkları ekle

            # Verileri TableWidget'a ekle
            for row_index, row_data in df_selected.iterrows():
                self.tableWidget.insertRow(row_index)  # Satır ekle
                for col_index, value in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(value))  # Hücreye değer ekle
                    self.tableWidget.setItem(row_index, col_index, item)

            self.tableWidget.setHorizontalScrollBarPolicy(
                QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff
            )  
            self.add_tooltips()

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                None, "Error", f"An error occurred while loading the data: {str(e)}"
            )
    
    def search_meetings(self):
        # Arama kutusundaki metne göre toplantilari filtreler
        search_text = (
            self.lineEditaramabosluk.text().lower().strip()
        )  # Kullanıcının girdiği arama metnini al

        if not search_text:  # Eğer arama boşsa, tüm verileri göster
            self.show_all_meetings()
            return

        try:
            # Excel dosyasını oku
            df = pd.read_excel("Files/Mentor.xlsx")

            # Sadece burdaki sütunları al
            selected_columns = [
                "Meeting Date",
                "Period",
                "Full Name",
                "Mentor",
                "Evaluation",
                "Current Status",
            ]
            df_selected = df[selected_columns]

            # İsimlerdeki boşlukları temizle
            df_selected["Full Name"] = df_selected[
                "Full Name"
            ].str.strip()  # İsimlerin başındaki ve sonundaki boşlukları kaldır

            # Arama metnine göre filtrele
            filtered_df = df_selected[
                df_selected["Full Name"].str.lower().str.startswith(search_text)
            ]  # İsimlerde arama metni ile başlayanları al

            # Duplicate kayıtları kaldır
            filtered_df = filtered_df.drop_duplicates(
                subset=["Full Name"], keep="first"
            )

            # TableWidget'ı temizle
            self.tableWidget.setRowCount(0)  # Eskiden eklenmiş veriler varsa temizle

            if filtered_df.empty:  # Eğer arama sonucu boşsa
                QtWidgets.QMessageBox.information(
                    None, "Information", "No records match the search criteria."
                )
                return

            # Başlıkları ayarla
            headers = filtered_df.columns.tolist()  # Başlıkları alıyoruz
            self.tableWidget.setColumnCount(
                len(headers)
            )  # TableWidget'ta sütun sayısını ayarla
            self.tableWidget.setHorizontalHeaderLabels(headers)  # Başlıkları ekle

            # Filtrelenmiş veriyi TableWidget'a ekliyoruz
            for row_data in filtered_df.itertuples(
                index=False, name=None
            ):  # Her satırı alıyoruz
                row_position = (
                    self.tableWidget.rowCount()
                )  # Mevcut satır sayısını alıyoruz
                self.tableWidget.insertRow(row_position)  # Yeni satır ekliyoruz
                for col_index, value in enumerate(
                    row_data
                ):  # Satırdaki her hücreyi ekliyoruz
                    item = QtWidgets.QTableWidgetItem(
                        str(value)
                    )  # Hücreye değer ekliyoruz
                    self.tableWidget.setItem(
                        row_position, col_index, item
                    )  # Hücreyi tabloya ekliyoruz

            # ToolTip ekle(mouse ile üzerine gelince tam metni göster)
            self.add_tooltips()

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                None, "Error", f"An error occurred during the search process: {str(e)}"
            )

    def add_tooltips(self):
        # Sadece 5. ve 6. sütunlara ToolTip ekle
        for row in range(self.tableWidget.rowCount()):
            for col in [4, 5]:  # 5. ve 6. sütunlar
                item = self.tableWidget.item(row, col)
                if item:
                    item.setToolTip(
                        item.text()
                    )  # Mouse ile üzerine gelince tam metni göster

    def return_to_menu(self):
        if hasattr(self, "main_window"):  # Eğer main_window tanımlıysa
            self.main_window.close() 
            self.windows_manager= WindowManager()  
        
        self.windows_manager.open_window("pam",role=self.role)
        

    def exit_application(self):
        # Uygulamayi kapatir
        sys.exit()

    def filter_data(self):
        # Verileri filtreler
        
        filter_meetings(self)  # filter_meetings fonksiyonunu çağırıyoruz
        self.add_tooltips() 

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
