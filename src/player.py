from pathlib import Path
import os
'''modules to work with files and paths'''


PLAYERS_LIST = ["mpv", "vlc", "mplayer"]
THE_PATH = "data/player.txt"


def is_valid(player_name):
    '''return True if player exist otherwise False'''
    if (player_name not in PLAYERS_LIST) or (os.stat(THE_PATH).st_size == 0):
        print("name or file is empty is valide")
        return False

    return True


def looping_asking(player):
    '''Keep asking for the right answer'''
    is_not_valid = True
    while is_not_valid:
        if is_valid(player) is False:
            player = input(
                "What is your default media player? (mpv, vlc, mplayer) : ").lower()
            with open(THE_PATH, mode="w", encoding='utf-8') as file:
                file.write(player)
        else:
            is_not_valid = False
    return player


def check_player():
    """takes no argument return name of the player"""
    path = Path(THE_PATH)
    if path.exists():
        print("File Exist")
        player = path.read_text(encoding='utf-8').lower()
        return looping_asking(player)
    else:
        print("File doesn't exist")
        path.touch(exist_ok=True)
        player = input(
            "What is your default media player? (mpv, vlc, mplayer) : ").lower()
        path.write_text(player, encoding='utf-8')

        print("success creating")
        return looping_asking(player)
