"""import cx_Freeze

executables = [cx_Freeze.Executable("alien_invasion.py")]

cx_Freeze.setup(
    name= 'Alien Invasion',
    options = {'build_exe': {'packages':['pygame'],
                             'incluide_files':['Alien.bmp','game_music.wav',
                                                'game_music.wav','high_score.txt',
                                                'pew.wav','bullet_1.bmp','start_blank.bmp',
                                                'start_easy.bmp','start_mid.bmp','start_hard.bmp',
                                                'exit.bmp','numbers.ttf','full_hearts.bmp',
                                                'two_hearts.bmp','one_hearts.bmp','zero_hearts.bmp','star_6.bmp']}},
    executables = executables
    )


"""