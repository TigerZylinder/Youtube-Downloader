import subprocess
import sys

# Liste der benötigten Bibliotheken
required_libraries = [
    'tkinter', 
    'ttkthemes', 
    'yt-dlp', 
    'json'  # 'json' ist eine eingebaute Bibliothek, daher ist sie nicht in der Liste nötig
]

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_libraries():
    for lib in required_libraries:
        try:
            __import__(lib)
            print(f"{lib} ist bereits installiert.")
        except ImportError:
            print(f"{lib} ist nicht installiert. Installation wird gestartet...")
            install_package(lib)

if __name__ == "__main__":
    check_and_install_libraries()
