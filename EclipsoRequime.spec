# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('augiepixel.ttf', '.'), ('Background.png', '.'), ('EclipsoRequimTitleBackground.png', '.'), ('PlayerSpriteLeft.png', '.'), ('PlayerSpriteRight.png', '.'), ('Monster1Frame1.png', '.'), ('Monster1Frame2.png', '.'), ('Monster1Frame3.png', '.'), ('Bullet.png', '.'), ('orbprojectile.png', '.'), ('jumpsoundeffect.mp3', '.'), ('shootsoundeffect.mp3', '.'), ('click.mp3', '.'), ('retro-hurt.mp3', '.'), ('cheering.mp3', '.')],
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
    name='EclipsoRequime',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
