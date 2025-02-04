
from PyQt6 import QtWidgets

class AdminMenu(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Menu")
        self.setGeometry(100, 100, 800, 500)

        label = QtWidgets.QLabel("Welcome to Admin Panel", self)
        label.setGeometry(250, 200, 300, 50)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = AdminMenu()
    window.show()
    app.exec()
