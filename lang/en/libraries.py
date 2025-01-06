import subprocess
import sys

# List of required libraries
required_libraries = [
    'tkinter', 
    'ttkthemes', 
    'yt-dlp', 
    'json'  # 'json' is a built-in library, so it does not need to be in the list
]

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_libraries():
    for lib in required_libraries:
        try:
            __import__(lib)
            print(f"{lib} is already installed.")
        except ImportError:
            print(f"{lib} is not installed. Installation will start...")
            install_package(lib)

if __name__ == "__main__":
    check_and_install_libraries()
