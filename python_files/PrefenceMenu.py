# Form implementation generated from reading ui file 'PrefenceMenu.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess


class Ui_Form(object):
    def setupUi(self, Form):
        self.parent_widget = Form
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(726, 510)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 1, 1, 1)
        self.pushButton_Exit = QtWidgets.QPushButton(parent=Form)
        self.pushButton_Exit.setEnabled(True)
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.gridLayout.addWidget(self.pushButton_Exit, 8, 1, 1, 1)
        self.title = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 1, 0, 1, 3)
        self.pushButton_Mentor_Meeting = QtWidgets.QPushButton(parent=Form)
        self.pushButton_Mentor_Meeting.setObjectName("pushButton_Mentor_Meeting")
        self.gridLayout.addWidget(self.pushButton_Mentor_Meeting, 5, 1, 1, 1)
        self.pushButton_Applications = QtWidgets.QPushButton(parent=Form)
        self.pushButton_Applications.setObjectName("pushButton_Applications")
        self.gridLayout.addWidget(self.pushButton_Applications, 2, 1, 1, 1)
        self.pushButton_Interviews = QtWidgets.QPushButton(parent=Form)
        self.pushButton_Interviews.setObjectName("pushButton_Interviews")
        self.gridLayout.addWidget(self.pushButton_Interviews, 6, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_Applications.clicked.connect(self.open_applications)
        self.pushButton_Mentor_Meeting.clicked.connect(self.open_mentormeeting)
        self.pushButton_Interviews.clicked.connect(self.open_interviews)
        self.pushButton_Exit.clicked.connect(self.exit)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Exit.setText(_translate("Form", "EXIT"))
        self.title.setText(_translate("Form", "PREFENCE MENU"))
        self.pushButton_Mentor_Meeting.setText(_translate("Form", "MENTOR MEETING"))
        self.pushButton_Applications.setText(_translate("Form", "APPLICATIONS"))
        self.pushButton_Interviews.setText(_translate("Form", "INTERWIEWS"))

    def open_applications(self):
        appPath = 'C:/Users/eren_/Desktop/CRM/python_files/applications_page.py'
        subprocess.Popen(["python", appPath])
        self.parent_widget.close()

    def open_mentormeeting(self):
        MentorPath = 'C:/Users/eren_/Desktop/CRM/python_files/mentor_interview.py'
        subprocess.Popen(["python", MentorPath])
        self.parent_widget.close()

    def open_interviews(self):
        interviewsPath = 'C:/Users/eren_/Desktop/CRM/python_files/interviews.py'
        subprocess.Popen(["python", interviewsPath])
        self.parent_widget.close()

    def exit(self):
        self.parent_widget.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())