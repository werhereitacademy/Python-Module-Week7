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
        image_path = os.path.join(current_dir, 'images/zemin-kucuk.jpg')
        
        # QPixmap kullanarak resmi QLabel'e yerleştiriyoruz
        pixmap = QtGui.QPixmap(image_path)
        if not pixmap.isNull():
            self.background_label.setPixmap(pixmap)
            self.background_label.setScaledContents(True)
        else:
            print(f"Resim yüklenemedi: {image_path}")
        
        self.Basvurular_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Basvurular_2.setGeometry(QtCore.QRect(300, 350, 141, 31))
        self.Basvurular_2.setAutoFillBackground(False)
        self.Basvurular_2.setStyleSheet("QPushButton{\n"
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
        self.Basvurular_2.setObjectName("Basvurular_2")
        
        self.Basvurular = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Basvurular.setGeometry(QtCore.QRect(80, 350, 141, 31))
        self.Basvurular.setAutoFillBackground(False)
        self.Basvurular.setStyleSheet("QPushButton{\n"
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
        self.Basvurular.setObjectName("Basvurular")
        
        self.Mentor = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Mentor.setGeometry(QtCore.QRect(560, 350, 181, 31))
        self.Mentor.setAutoFillBackground(False)
        self.Mentor.setStyleSheet("QPushButton{\n"
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
        self.Mentor.setObjectName("Mentor")
        
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 540, 91, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setObjectName("pushButton")
        
        self.Adminmenu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Adminmenu.setGeometry(QtCore.QRect(440, 280, 141, 31))
        self.Adminmenu.setAutoFillBackground(False)
        self.Adminmenu.setStyleSheet("QPushButton{\n"
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
        self.Adminmenu.setObjectName("Adminmenu")
        
        self.Anamenu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Anamenu.setGeometry(QtCore.QRect(190, 280, 141, 31))
        self.Anamenu.setAutoFillBackground(False)
        self.Anamenu.setStyleSheet("QPushButton{\n"
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
        self.Anamenu.setObjectName("Anamenu")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Basvurular_2.setText(_translate("MainWindow", "MÜLAKATLAR"))
        self.Basvurular.setText(_translate("MainWindow", "BAŞVURULAR"))
        self.Mentor.setText(_translate("MainWindow", "MENTÖR GÖRÜŞMESİ"))
        self.pushButton.setText(_translate("MainWindow", "KAPAT"))
        self.Adminmenu.setText(_translate("MainWindow", "ADMIN MENÜ"))
        self.Anamenu.setText(_translate("MainWindow", "ANA MENÜ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
