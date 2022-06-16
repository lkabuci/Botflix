from rich import print
from rich.console import Console
import requests

import os
from pathlib import Path



PLAYERS_LIST = ["mpv", "vlc", "mplayer"]
CONFIG_PATH = "config/player.txt"

console = Console()


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
    

def handle_erros(url: str):
    # ASK your Aquib to test the requests error! to handle the VPN situation
    # Connection Error if i'm not connected to the internet

    
    try:
        requests.get(url)

    except requests.exceptions.ConnectionError:
        console.print("[bold red]ERR_INTERNET_DISCONNECTED[red bold]")

    except requests.exceptions.HTTPError:
        console.print(
            "[bold red]The wesite is probably prohibited in your country please consider using a VPN[bold red]"
        )
        exit()

    except requests.exceptions.RequestException as err:
        print(err)
        exit()
    
    
# print(":right_arrow:")