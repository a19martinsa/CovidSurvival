# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
import sys

a = Analysis(['covidSurvival.py'],
             pathex=['C:\\Prueba_pyinstaller\\CovidSurvival'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas + [   ('database.db', 'database.db', 'DATA'),
                        ('imagenes/covid2.png', 'imagenes/covid2.png', 'DATA'),
                        ('imagenes/jugador2.png', 'imagenes/jugador2.png', 'DATA'),
                        ('imagenes/jugador3.png', 'imagenes/jugador3.png', 'DATA'),
                        ('imagenes/jugador4.jpg', 'imagenes/jugador4.jpg', 'DATA'),
                        ('imagenes/jugador5.png', 'imagenes/jugador5.png', 'DATA'),
                        ('imagenes/jugador6.jpg', 'imagenes/jugador6.jpg', 'DATA'),
                        ('musica/arex.ogg', 'musica/arex.ogg', 'DATA'),
                        ('musica/batalla.ogg', 'musica/batalla.ogg', 'DATA'),
                        ('musica/biological.ogg', 'musica/biological.ogg', 'DATA'),
                        ('musica/ending.ogg', 'musica/ending.ogg', 'DATA'),
                        ('musica/heroic.ogg', 'musica/heroic.ogg', 'DATA'),
                        ('musica/planeta.ogg', 'musica/planeta.ogg', 'DATA'),
                        ('musica/resilience.ogg', 'musica/resilience.ogg', 'DATA')
                    ],
          name=os.path.join('dist','CovidSurvival'+('.exe' if sys.platform == 'win32' else '')),
          debug=False,
          bootloader_ignore_signals=False,
          strip=None,
          upx=True,
          runtime_tmpdir=None,
          console=False ,
          icon='imagenes/tree.ico')
