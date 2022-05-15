from rich import print

import os
from pathlib import Path


PLAYERS_LIST = ["mpv", "vlc", "mplayer"]
CONFIG_PATH = "config/player.txt"


def clear_screen() -> None:
    os.system("clear") if os.name == "posix" else os.system("cls")


def is_player_valid() -> bool:
    """return True if player exist otherwise False"""
    try:
        player_name = Path(CONFIG_PATH).read_text()

    except FileNotFoundError as e:
        print(f"{e}\n[bold yellow]Try python3 main.py config [/bold yellow]")
        exit(1)

    else:
        # the second argument is to check if the file is empty
        if (player_name not in PLAYERS_LIST) or (os.stat(CONFIG_PATH).st_size == 0):
            return False

    return True


def wrong_player(player):
    print(f"[bold red]Operation failed [u]{player}[/u] is not a valid player[bold red]")
    print(
        "[bold yellow]Hint: the supported players are vlc, mpv and mplayer[/bold yellow]"
    )
    print("[bold]Try again with one of the supported players[/bold]")
    exit(1)
