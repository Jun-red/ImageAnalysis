import sys
from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = [
        '--onefile',
        '--windowed',
        '--icon=images/company_logo.png',
        'main.py'
    ]
    sys.exit(run(opts))