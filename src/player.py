from typing import Callable
from pathlib import Path
import os

# supported video player
PLAYERS_LIST = ["mpv", "vlc", "mplayer"]
THE_PATH = "data/player.txt"


def is_valid(player_name: str) -> bool:
    '''return True if player exist otherwise False'''

    # the second argument is to check if the file is empty
    if (player_name not in PLAYERS_LIST) or (os.stat(THE_PATH).st_size == 0):
        return False

    return True


def keep_asking(player: str) -> str:
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


def check_player() -> Callable[[str], str]:
    """takes no argument return name of the player"""
    path = Path(THE_PATH)
    if path.exists():
        player = path.read_text(encoding='utf-8').lower()
        return keep_asking(player)
    else:
        path.touch(exist_ok=True)
        player = input(
            "What is your default media player? (mpv, vlc, mplayer) : ").lower()
        path.write_text(player, encoding='utf-8')

        return keep_asking(player)

