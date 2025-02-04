
from PyQt6 import QtWidgets

class UserMenu(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Menu")
        self.setGeometry(100, 100, 800, 500)

        label = QtWidgets.QLabel("Welcome to User Panel", self)
        label.setGeometry(250, 200, 300, 50)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = UserMenu()
    window.show()
    app.exec()