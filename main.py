import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from login_page import LoginPage
from user_list_page import UserListPage
from book_list_page import BookListPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyQt6 Python Projesi")
        self.setGeometry(100, 100, 400, 300)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Sayfaları oluştur ve stacked_widget'e ekle
        self.login_page = LoginPage(self.stacked_widget)
        self.user_list_page = UserListPage(self.stacked_widget)
        self.book_list_page = BookListPage(self.stacked_widget)

        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.user_list_page)
        self.stacked_widget.addWidget(self.book_list_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())