import os
from pathlib import Path

import requests
from rich import print
from rich.console import Console

PLAYERS_LIST = ["mpv", "vlc", "mplayer"]
PLAYER_FILE = "player.txt"

console = Console()


def clear_screen() -> None:
    os.system("clear") if os.name == "posix" else os.system("cls")


def is_player_valid() -> bool:
    """return True if player is valid otherwise False"""

    try:
        player_name = Path(PLAYER_FILE).read_text()
    except FileNotFoundError:
        return False
    if (player_name not in PLAYERS_LIST) or (os.stat(PLAYER_FILE).st_size == 0):
        return False

    # Check if player is in windows path
    if os.name == "nt":
        for exec_path in os.get_exec_path():
            if any(
                player_name.lower()
                in list(map(lambda x: x.lower(), exec_path.split(os.sep)))
            ):
                return True
        else:
            print(f"[bold red]{player_name} is not in your path[bold red]")
            return False
    return True


def handle_errors(url: str):
    clear_screen()
    try:
        requests.get(url)

    except requests.exceptions.ConnectionError:
        console.print("[bold red]ERR_INTERNET_DISCONNECTED[red bold]")

    except requests.exceptions.HTTPError:
        console.print(
            "[bold red]The host is probably banned in your country please consider using a VPN or choose another "
            "host[bold red] "
        )
        exit()

    except requests.exceptions.RequestException as err:
        print(err)
        exit()


def set_player(name: str):
    player = Path(PLAYER_FILE)
    player.write_text(name)


def get_player() -> str:
    player = Path(PLAYER_FILE)
    if player.exists():
        return player.read_text()
    else:
        print("[red bold]You need to setup a default player first[bold red]")
