import sys
from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = [
        '--onefile',
        '--windowed',
        '--icon=../images/logo.jpg',
        '../main.py'
    ]
    sys.exit(run(opts))
