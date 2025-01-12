# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('setting.ini', 'setting.ini')],  # setting.ini を含める
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=True,  # これを True にすると、より軽量になります
)

pyz = PYZ(a.pure, a.zipped_data,
    cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=False,
    name='your_program_name',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,  # これを True にすると、実行ファイルが軽量化されます
    upx=True,  # UPX で圧縮し、軽量化します
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # これによりコンソールが非表示になります
    icon='icon.ico'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=True,
    upx=True,
    upx_exclude=[],
    name='your_program_name'
)
