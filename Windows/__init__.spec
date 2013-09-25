# -*- mode: python -*-
a = Analysis(['__init__.py'],
             pathex=['C:\\Users\\Matheus\\Documents\\Controle de acesso\\ controle-de-acesso-2\\controle-de-acesso-2\\trunk'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='__init__.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='__init__')
