from typing import List
import subprocess

from rich.console import Console
console = Console()

def get_magnet(magnets: List[str]) -> str:
    '''takes magnets list, return the chosen magnet'''
    
    is_valid = True
    while is_valid:
        number = int(console.input("[bold i]Enter Your Choice: [bold i]"))
        if (number > len(magnets)) or (number <= 0):
            print("\033[91m Invalid choice. \033[0m")
        else:
            is_valid = False

    # actual index starts 0 --> 13
    # but the table shows 1 --> 14
    # -1 to select from 1 --> 14
    return magnets[number - 1]


def stream(magnet: str, default_player: str) -> None:
    '''tages a chosen magnet and a deafult player
    run the process.
    '''
    
    subprocess.run(["webtorrent", magnet, f"--{default_player}"], check=True)
