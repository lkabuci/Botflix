import os
from typing import List

from rich.console import Console

console = Console()


def get_magnet(magnets: List[str]) -> str:
    """takes magnets list, return the chosen magnet"""

    number = -1
    magnet_count = len(magnets)
    while (number < 0) or (number > magnet_count):
        try:
            number = int(
                console.input(
                    "[bold i]Enter Your Choice (or 0 if you want to quit): [bold i]"
                )
            )
            if (number < 0) or (number > magnet_count):
                console.print(
                    f"[red]Your choice must be between 0 (quit) and {magnet_count}.[red]"
                )
        except Exception:
            console.print("[red]Invalid input.[red]")
    if number == 0:
        console.print("[red]Quitting...[red]")
        exit()
    else:
        # actual index starts 0 --> 13
        # but the table shows 1 --> 14
        # -1 to select from 1 --> 14
        return magnets[number - 1]


def stream(magnet: str, default_player: str) -> None:
    """takes a chosen magnet and a default player
    run the process.
    """

    try:
        os.system(f'webtorrent "{magnet}" --{default_player}')
    except Exception as e:
        print(e)
        print(f"[red bold]Error: {default_player} is not in your PATH!", end="\n")
        print("Please consider adding the default player to the right path", end="\n")
        print("Quitting... [/red bold]")
        exit(1)
