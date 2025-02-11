from login import UI_login
from PyQt6 import QtWidgets, QtCore
from backend.quickstart import download
import sys



class DownloadThread(QtCore.QThread):
    def run(self):
        download()  # İndirme işlemi arka planda çalışacak

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_login()  
    ui.setupUi(MainWindow)  
    MainWindow.show()  

    # Arka planda download başlat
    thread = DownloadThread()
    thread.start()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
