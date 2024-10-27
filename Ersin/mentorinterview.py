from PyQt6 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Arka plan için QLabel kullanarak resmi yükle
        self.background_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        
        # Resmin tam yolunu almak için os.path kullanıyoruz
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, 'images/zemin_buyuk.jpg')  # Dosya yolunu kendi dizinine göre ayarlayın
        
        # QPixmap kullanarak resmi QLabel'e yerleştiriyoruz
        pixmap = QtGui.QPixmap(image_path)
        if not pixmap.isNull():
            self.background_label.setPixmap(pixmap)
            self.background_label.setScaledContents(True)
        else:
            print(f"Resim yüklenemedi: {image_path}")
        
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(750, 340, 800, 600))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.Basvurular = QtWidgets.QPushButton(parent=self.frame)
        self.Basvurular.setGeometry(QtCore.QRect(80, 350, 141, 31))
        self.Basvurular.setAutoFillBackground(False)
        self.Basvurular.setStyleSheet("background-color:#05a90c; font-size:12pt; color:white")
        self.Basvurular.setObjectName("Basvurular")

        self.Mentor = QtWidgets.QPushButton(parent=self.frame)
        self.Mentor.setGeometry(QtCore.QRect(560, 350, 181, 31))
        self.Mentor.setAutoFillBackground(False)
        self.Mentor.setStyleSheet("background-color:#4d0094; font-size:12pt; color:white")
        self.Mentor.setObjectName("Mentor")

        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(700, 540, 91, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color:#800000; font-size:12pt; color:white")
        self.pushButton.setObjectName("pushButton")

        self.Adminmenu = QtWidgets.QPushButton(parent=self.frame)
        self.Adminmenu.setGeometry(QtCore.QRect(440, 280, 141, 31))
        self.Adminmenu.setAutoFillBackground(False)
        self.Adminmenu.setStyleSheet("background-color:#7d003b; font-size:12pt; color:white")
        self.Adminmenu.setObjectName("Adminmenu")

        self.Anamenu = QtWidgets.QPushButton(parent=self.frame)
        self.Anamenu.setGeometry(QtCore.QRect(190, 280, 141, 31))
        self.Anamenu.setAutoFillBackground(False)
        self.Anamenu.setStyleSheet("background-color:#363636; font-size:12pt; color:white")
        self.Anamenu.setObjectName("Anamenu")

        # Diğer bileşenler
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 70, 311, 31))
        self.label.setStyleSheet("QLabel{\n"
"color:white;\n"
"font-size:36px;\n"
"font-weight:bold;\n"
"background:none\n"
"}\n"
"")
        self.label.setObjectName("label")

        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 120, 800, 41))
        self.widget.setStyleSheet("QWidget{\n"
"color:black;\n"
"background:#d3d3d3;\n"
"opacity: 0.5;\n"
"font-weight:bold;\n"
"}")
        self.widget.setObjectName("widget")

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 10, 75, 24))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color:black;\n"
"background:white;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}\n"
"QPushButton::hover{\n"
"color:white;\n"
"background:#47545a;\n"
"border-radius:10px;\n"
"font-weight:bold\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 241, 22))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"color:black;\n"
"background:white;\n"
"font-weight:bold;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 10, 201, 24))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"color:black;\n"
"background:white;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}\n"
"QPushButton::hover{\n"
"color:white;\n"
"background:#47545a;\n"
"border-radius:10px;\n"
"font-weight:bold\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")

        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(510, 170, 281, 22))
        self.comboBox.setStyleSheet("QComboBox{\n"
"color:black;\n"
"background:white;\n"
"font-weight:bold;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.tableView = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(0, 200, 800, 341))
        self.tableView.setStyleSheet("QTableView{\n"
"color:black;\n"
"background:white;\n"
"font-weight:bold;\n"
"}")
        self.tableView.setObjectName("tableView")

        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(720, 545, 75, 30))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background:red;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}\n"
"QPushButton::hover{\n"
"color:white;\n"
"background:#47545a;\n"
"border-radius:10px;\n"
"font-weight:bold\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 170, 91, 24))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"color:black;\n"
"background:white;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}\n"
"QPushButton::hover{\n"
"color:white;\n"
"background:#47545a;\n"
"border-radius:10px;\n"
"font-weight:bold\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Basvurular.setText(_translate("MainWindow", "BAŞVURULAR"))
        self.Mentor.setText(_translate("MainWindow", "MENTÖR GÖRÜŞMESİ"))
        self.pushButton.setText(_translate("MainWindow", "KAPAT"))
        self.Adminmenu.setText(_translate("MainWindow", "ADMIN MENÜ"))
        self.Anamenu.setText(_translate("MainWindow", "ANA MENÜ"))
        self.label.setText(_translate("MainWindow", "Mentor Interview"))
        self.pushButton_2.setText(_translate("MainWindow", "BUL"))
        self.lineEdit.setText(_translate("MainWindow", "ARANACAK METNİ GİRİNİZ"))
        self.pushButton_3.setText(_translate("MainWindow", "TÜM GÖRÜŞMELER"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Vıt Projesinin Tamamına Katılması Uygun Olur"))
        self.comboBox.setItemText(1, _translate("MainWindow", "VIT Projesi ilk IT Eğtimi Al... ya Yönlendirilmesi Uygun Olur"))
        self.comboBox.setItemText(2, _translate("MainWindow", "VIT Projesi İngilizce Eğtimi Al... ya Yönlendirilmesi Uygun Olur"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Vit Pojesi Kapsamında Dir.. Yönlendirilmesi Uygun Olur"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Direkt Bireysel Koçluk İle İşe Yönlendirilmesi Uygun Olur"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Bir Sonraki VIT Projesine Katılması Daha Uygun Olur"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Başka Bir Sektöre Yönlendirilmesi"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Diğer"))
        self.pushButton_4.setText(_translate("MainWindow", "KAPAT"))
        self.pushButton_5.setText(_translate("MainWindow", "TERCİHLER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
