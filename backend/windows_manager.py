from PyQt6 import QtWidgets





import importlib

class WindowManager:
    def __init__(self):
        self.window = None  # Pencereyi tutacak değişken
        self.ui = None      # UI sınıfı

    def open_window(self, ui_class_name: str,role=None):
        """
        Verilen sayfa ismi ile yeni bir pencere aç.
        ui_class_name: Sayfa sınıfının ismi (örneğin: "login", "deneme", vb.)
        """

        
        modeles={
                 "login":{"model":"login","UI":"UI_login"},
                 "pam":{"model":"preference","UI":"UI_Pam"},
                 "applications":{"model":"applications","UI":"Ui_Application_Menu"},
                 "mentor":{"model":"mentor","UI":"Ui_MainWindow"},
                 "admin":{"model":"admin","UI":"Ui_MainWindow"},
                 "interviews":{"model":"interviews","UI":"UI_Im"},                 

                 
                 
                 
                 
                 }

        try:
            
            # Sayfa sınıfını dinamik olarak import et
            module_name = ui_class_name.lower()  # Modül ismini küçük harflerle al
            print(modeles[module_name]["model"])
            print(modeles[module_name]["UI"])
            module = importlib.import_module(modeles[module_name]["model"])  # Modülü import et
            ui_class = getattr(module, modeles[module_name]["UI"])  # Modülden sınıfı al
            print(module)
            # Yeni pencereyi oluştur
            self.window = QtWidgets.QMainWindow()
            self.ui = ui_class(role)  # UI sınıfını oluştur
            print(self.ui)
            self.ui.setupUi(self.window)
            self.window.show()
        except ModuleNotFoundError:
            print(f"Hata: {ui_class_name} modülü bulunamadı.")
        except AttributeError as e:
            print(e)