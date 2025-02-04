import sys
import os

# PyBackend klasörünün tam yolunu al
pybackend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "PyBackend"))

# PyBackend klasörünün olup olmadığını ve içinde login_b.py'nin var olup olmadığını kontrol edin
if os.path.isdir(pybackend_path):
    print(f"PyBackend path found: {pybackend_path}")
    if os.path.isfile(os.path.join(pybackend_path, "login_b.py")):
        print("login_b.py found.")
    else:
        print("Error: 'login_b.py' not found in PyBackend.")
    # PyBackend klasörünü Python'un import yoluna ekle
    sys.path.append(pybackend_path)
else:
    print(f"Error: '{pybackend_path}' directory not found.")

# PyBackend klasöründeki login_b modülünü import et
try:
    import login_b
    print("login_b imported successfully.")
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundError: {e}")

if __name__ == "__main__":
    # login_b içindeki start_login_app fonksiyonunu çağır
    login_b.start_login_app()
