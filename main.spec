# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('images/rocket_48x48.png', 'img'), ('images/china.png', 'img'), ('images/home2 - 副本.png', 'img'), ('images/video-camera.png', 'img'), ('images/file-video.png', 'img'), ('images/data-transfer.png', 'img'), ('images/location-crosshairs.png', 'img'), ('images/usb-pendrive.png', 'img'), ('images/user (1).png', 'img'), ('images/github (1) - 副本.png', 'img'), ('images/viber - 副本 (2).png', 'img'), ('images/power - 副本.png', 'img'), ('images/setting.png', 'img'), ('images/save.png', 'img'), ('images/power_start.png', 'img'), ('images/power-on.png', 'img'), ('images/broken-link (1).png', 'img'), ('images/broken-link.png', 'img'), ('images/man.png', 'img')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['images\\logo.jpg'],
)
