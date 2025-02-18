# Form implementation generated from reading ui file 'prefences_admin.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_prefences_admin_applications = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_prefences_admin_applications.setGeometry(QtCore.QRect(170, 170, 171, 40))
        self.pushButton_prefences_admin_applications.setStyleSheet("QPushButton {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: 14pt \"Symbol\";\n"
"    color: black; /* Siyah yazı rengi */\n"
"    background: rgba(0, 84, 147, 128);\n"
"    border-radius: 2px; /* Köşe yuvarlama */\n"
"    padding: 8px; /* Küçük padding */\n"
"    border: 1px solid black; /* İnce siyah çerçeve */\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(145, 145, 145); \n"
"    /* Hover durumunda gölgeyi değiştirmek için */\n"
"}")
        self.pushButton_prefences_admin_applications.setObjectName("pushButton_prefences_admin_applications")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 70, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 28pt \"Symbol\";")
        self.label.setObjectName("label")
        self.pushButton_prefences_admin_exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_prefences_admin_exit.setGeometry(QtCore.QRect(170, 390, 441, 40))
        self.pushButton_prefences_admin_exit.setStyleSheet("QPushButton {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: 14pt \"Symbol\";\n"
"    color: black; /* Siyah yazı rengi */\n"
"    background: rgba(0, 84, 147, 128);\n"
"    border-radius: 2px; /* Köşe yuvarlama */\n"
"    padding: 8px; /* Küçük padding */\n"
"    border: 1px solid black; /* İnce siyah çerçeve */\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(145, 145, 145); \n"
"    /* Hover durumunda gölgeyi değiştirmek için */\n"
"}")
        self.pushButton_prefences_admin_exit.setObjectName("pushButton_prefences_admin_exit")
        self.pushButton__prefences_admin_interviews = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton__prefences_admin_interviews.setGeometry(QtCore.QRect(170, 260, 171, 40))
        self.pushButton__prefences_admin_interviews.setStyleSheet("QPushButton {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: 14pt \"Symbol\";\n"
"    color: black; /* Siyah yazı rengi */\n"
"    background: rgba(0, 84, 147, 128);\n"
"    border-radius: 2px; /* Köşe yuvarlama */\n"
"    padding: 8px; /* Küçük padding */\n"
"    border: 1px solid black; /* İnce siyah çerçeve */\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(145, 145, 145); \n"
"    /* Hover durumunda gölgeyi değiştirmek için */\n"
"}")
        self.pushButton__prefences_admin_interviews.setObjectName("pushButton__prefences_admin_interviews")
        self.pushButton_prefences_admin_main_menu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_prefences_admin_main_menu.setGeometry(QtCore.QRect(170, 340, 441, 40))
        self.pushButton_prefences_admin_main_menu.setStyleSheet("QPushButton {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: 14pt \"Symbol\";\n"
"    color: black; /* Siyah yazı rengi */\n"
"    background: rgba(0, 84, 147, 128);\n"
"    border-radius: 2px; /* Köşe yuvarlama */\n"
"    padding: 8px; /* Küçük padding */\n"
"    border: 1px solid black; /* İnce siyah çerçeve */\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(145, 145, 145); \n"
"    /* Hover durumunda gölgeyi değiştirmek için */\n"
"}")
        self.pushButton_prefences_admin_main_menu.setObjectName("pushButton_prefences_admin_main_menu")
        self.pushButton__prefences_admin_mentor_interview = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton__prefences_admin_mentor_interview.setGeometry(QtCore.QRect(440, 170, 171, 40))
        self.pushButton__prefences_admin_mentor_interview.setStyleSheet("QPushButton {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: 14pt \"Symbol\";\n"
"    color: black; /* Siyah yazı rengi */\n"
"    background: rgba(0, 84, 147, 128);\n"
"    border-radius: 2px; /* Köşe yuvarlama */\n"
"    padding: 8px; /* Küçük padding */\n"
"    border: 1px solid black; /* İnce siyah çerçeve */\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(145, 145, 145); \n"
"    /* Hover durumunda gölgeyi değiştirmek için */\n"
"}")
        self.pushButton__prefences_admin_mentor_interview.setObjectName("pushButton__prefences_admin_mentor_interview")
        self.pushButton_i_prefences_admin_menu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_i_prefences_admin_menu.setGeometry(QtCore.QRect(440, 260, 171, 40))
        self.pushButton_i_prefences_admin_menu.setStyleSheet("QPushButton {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: 14pt \"Symbol\";\n"
"    color: black; /* Siyah yazı rengi */\n"
"    background: rgba(0, 84, 147, 128);\n"
"    border-radius: 2px; /* Köşe yuvarlama */\n"
"    padding: 8px; /* Küçük padding */\n"
"    border: 1px solid black; /* İnce siyah çerçeve */\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(145, 145, 145); \n"
"    /* Hover durumunda gölgeyi değiştirmek için */\n"
"}")
        self.pushButton_i_prefences_admin_menu.setObjectName("pushButton_i_prefences_admin_menu")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_prefences_admin_applications.setText(_translate("MainWindow", "APPLICATIONS"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">PREFENCES -ADMIN</span></p></body></html>"))
        self.pushButton_prefences_admin_exit.setText(_translate("MainWindow", "EXIT"))
        self.pushButton__prefences_admin_interviews.setText(_translate("MainWindow", "INTERVIEWS"))
        self.pushButton_prefences_admin_main_menu.setText(_translate("MainWindow", "MAIN MENU"))
        self.pushButton__prefences_admin_mentor_interview.setText(_translate("MainWindow", "MENTOR INTERVIEW"))
        self.pushButton_i_prefences_admin_menu.setText(_translate("MainWindow", "ADMIN MENU"))
