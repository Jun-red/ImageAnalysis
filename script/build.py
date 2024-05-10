import sys
from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = [
        '--onefile',
        '--windowed',
        '--icon=C:\\Users\\12284\\Desktop\\GitHub\\ImageAnalysis\\images\\china.png',
        'C:\\Users\\12284\\Desktop\\GitHub\\ImageAnalysis\\main.py'
    ]
    sys.exit(run(opts))
        