import sys
import os

# PyBackend klasörünün tam yolunu al
pybackend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "PyBackend"))

sys.path.append(pybackend_path)
import login_b

if __name__ == "__main__":
    # login_b içindeki start_login_app fonksiyonunu çağır
    login_b.start_login_app()
