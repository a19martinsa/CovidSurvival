import cx_Freeze

executables = [cx_Freeze.Executable("evasor.py")]

cx_Freeze.setup(
    name="EvasorMM",
    options={"build_exe": {"packages": ["pygame", "os"],
                           "include_files": ["jugador2.png", "musica1.mp3", "covid2.png", "gobierno.mp3",
                                             "juegoterminado.wav", "villano2.png",
                                             'InTE.mp3', 'CastleOG.mp3', 'Numb.mp3', 'Nigths.mp3', 'Counting.mp3',
                                             'Demons.mp3', '7years.mp3'],
                           "include_msvcr": True}},
    executables=executables

)
