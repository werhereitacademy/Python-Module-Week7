from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QCompleter, QTableWidgetItem
import json,sys
from PrefenceAdminMenu import Ui_Form_Admin
from PrefenceMenu import Ui_Form





class Ui_interviewsWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 569)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.columnView = QtWidgets.QTableWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.columnView.sizePolicy().hasHeightForWidth())
        self.columnView.setSizePolicy(sizePolicy)
        self.columnView.setLineWidth(0)
        self.columnView.setMidLineWidth(0)
        self.columnView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.columnView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.columnView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.columnView.setIconSize(QtCore.QSize(0, 150))
        self.columnView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerItem)
        self.columnView.setGridStyle(QtCore.Qt.PenStyle.NoPen)
        self.columnView.setCornerButtonEnabled(True)
        self.columnView.setColumnCount(3)
        self.columnView.setObjectName("columnView")
        self.columnView.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.columnView.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.columnView.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.columnView.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.columnView)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(50, -1, 10, 10)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_exit = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_exit.sizePolicy().hasHeightForWidth())
        self.pushButton_exit.setSizePolicy(sizePolicy)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.gridLayout.addWidget(self.pushButton_exit, 5, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.pushButton_project_sended = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_project_sended.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_project_sended.sizePolicy().hasHeightForWidth())
        self.pushButton_project_sended.setSizePolicy(sizePolicy)
        self.pushButton_project_sended.setObjectName("pushButton_project_sended")
        self.gridLayout.addWidget(self.pushButton_project_sended, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.pushButton_search = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_search.sizePolicy().hasHeightForWidth())
        self.pushButton_search.setSizePolicy(sizePolicy)
        self.pushButton_search.setMinimumSize(QtCore.QSize(93, 28))
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 3, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.pushButton_project_in = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_project_in.sizePolicy().hasHeightForWidth())
        self.pushButton_project_in.setSizePolicy(sizePolicy)
        self.pushButton_project_in.setObjectName("pushButton_project_in")
        self.gridLayout.addWidget(self.pushButton_project_in, 4, 3, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.pushButton_prefence = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_prefence.sizePolicy().hasHeightForWidth())
        self.pushButton_prefence.setSizePolicy(sizePolicy)
        self.pushButton_prefence.setObjectName("pushButton_prefence")
        self.gridLayout.addWidget(self.pushButton_prefence, 5, 3, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.lineEdit_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_input.sizePolicy().hasHeightForWidth())
        self.lineEdit_input.setSizePolicy(sizePolicy)
        self.lineEdit_input.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_input.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.gridLayout.addWidget(self.lineEdit_input, 3, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 854, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.columnView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.columnView.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name Surname"))
        item = self.columnView.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Project Submission Date"))
        item = self.columnView.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Project Development Date"))
        self.pushButton_exit.setText(_translate("MainWindow", "EXIT"))
        self.pushButton_project_sended.setText(_translate("MainWindow", "Projects Sent"))
        self.label.setText(_translate("MainWindow", "INTERVIEWS"))
        self.pushButton_search.setText(_translate("MainWindow", "SEARCH"))
        self.pushButton_project_in.setText(_translate("MainWindow", "Projects Received"))
        self.pushButton_prefence.setText(_translate("MainWindow", "Preferences"))
        self.lineEdit_input.setPlaceholderText(_translate("MainWindow", "Enter text to search.."))


        #calling methods
        self.setup_completer()
        self.pushButton_search.clicked.connect(self.search_data)
        self.pushButton_project_sended.clicked.connect(self.sended)
        self.pushButton_project_in.clicked.connect(self.arrived)
        self.pushButton_exit.clicked.connect(self.exit)
        self.pushButton_prefence.clicked.connect(self.preference)

    def jsonData(self):
        jsonPath = r'coverted_files\Mulakatlar.json'
        with open(jsonPath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    
    def roleJson(self):
        jsonPath = r"python_files\role.json"
        with open(jsonPath, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data
            

    def setup_completer(self):
        data = self.jsonData()
        names = [entry["Adınız Soyadınız"] for entry in data]
        completer = QCompleter(names)
        completer.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.lineEdit_input.setCompleter(completer)

    def search_data(self):
        data = self.jsonData()
        search_name = self.lineEdit_input.text().lower()
        if not search_name:
            return
        found = False
        for entry in data:
            if search_name in entry["Adınız Soyadınız"].lower():
                self.update_table(entry)
                found = True
                break
        if not found:
            self.clear_table()

    def update_table(self, entry):
        self.columnView.setRowCount(1)
        self.columnView.setItem(0, 0, QTableWidgetItem(entry["Adınız Soyadınız"]))
        self.columnView.setItem(0, 1, QTableWidgetItem(entry["Proje gonderilis tarihi"]))
        self.columnView.setItem(0, 2, QTableWidgetItem(entry["Projenin gelis tarihi"]))


    def clear_table(self):
        self.columnView.setRowCount(0)


    def sended(self):
        jsonData = self.jsonData()
        sendedItem = [item for item in jsonData if item["Proje gonderilis tarihi"]]
        self.columnView.setRowCount(len(sendedItem))
        for i,j in enumerate(sendedItem):
            self.columnView.setItem(i, 0, QTableWidgetItem(str(j.get("Adınız Soyadınız"))))
            self.columnView.setItem(i, 1, QTableWidgetItem(str(j.get("Proje gonderilis tarihi"))))
            self.columnView.setItem(i, 2, QTableWidgetItem(str(j.get("Projenin gelis tarihi"))))

    def arrived(self):
        jsonData = self.jsonData()
        arrivedItem = [item for item in jsonData if item['Projenin gelis tarihi']]
        self.columnView.setRowCount(len(arrivedItem))
        for i,j in enumerate(arrivedItem):
            self.columnView.setItem(i, 0, QTableWidgetItem(str(j.get("Adınız Soyadınız"))))
            self.columnView.setItem(i, 1, QTableWidgetItem(str(j.get("Proje gonderilis tarihi"))))
            self.columnView.setItem(i, 2, QTableWidgetItem(str(j.get("Projenin gelis tarihi"))))

    def exit(self):
        QtWidgets.QApplication.quit()

    def preference(self):
        state = self.roleJson()
        if state["login"] == "admin":  
            self.userWindow = QtWidgets.QWidget()
            self.user_ui = Ui_Form_Admin()
            self.user_ui.setupUi(self.userWindow)
            self.userWindow.show()
            MainWindow.close() 
        elif state["login"] == "user":
            self.adminWindow = QtWidgets.QWidget()
            self.adminUi = Ui_Form()
            self.adminUi.setupUi(self.adminWindow)
            self.adminWindow.show()
            MainWindow.close()
        else:
            print("calismadi")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_interviewsWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
