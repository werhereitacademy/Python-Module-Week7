from PyQt6 import QtCore, QtGui, QtWidgets,uic
import sys
class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        uic.loadUi('mavi.ui', self)
        self.show()
        self.pushButton_2.clicked.connect(self.pager)
    def pager(self):
            from yesil import Yesil_window
            self.cams = Yesil_window()
            self.cams.show()
            self.close()