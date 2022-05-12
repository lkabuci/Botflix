from typing import List
import subprocess

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
        return magnets[number - 1]
        # actual index starts 0 --> 13
        # but the table shows 1 --> 14
        # -1 to select from 1 --> 14


def stream(magnet: str, default_player: str) -> None:
    """tages a chosen magnet and a deafult player
    run the process.
    """

    subprocess.run(["webtorrent", magnet, f"--{default_player}"], check=True)
