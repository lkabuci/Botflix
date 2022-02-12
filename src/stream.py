import subprocess

def selection(magnet):
    '''takes magnet list, return the chosen magnet'''

    length = [item for item in range(len(magnet))]
    # is_invalid = True
    # TODO: re ask for a valid answer

    number = int(input("Enter Your Choice: "))
    if number > len(length):
        print("\033[91mInvalid input. Exiting...\033[0m")
        exit(0)
    return magnet[number]


def stream(magnet, default_player):
    '''tages a chosen magnet and a deafult player
    run the process.
    '''
    
    subprocess.run(["webtorrent", magnet, f"--{default_player}"], check=True)