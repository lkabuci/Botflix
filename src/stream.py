from typing import List
import subprocess

def get_magnet(magnets: List[str]) -> str:
    '''takes magnets list, return the chosen magnet'''

    # is_invalid = True
    # TODO: re ask for a valid answer

    number = int(input("Enter Your Choice: ")) + 1 # the table shown start from index 1 not 0
    if number > len(magnets):
        print("\033[91mInvalid input. Exiting...\033[0m")
        exit(0)

    return magnets[number]


def stream(magnet: str, default_player: str) -> None:
    '''tages a chosen magnet and a deafult player
    run the process.
    '''
    
    subprocess.run(["webtorrent", magnet, f"--{default_player}"], check=True)