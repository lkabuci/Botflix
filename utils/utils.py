from pathlib import Path
import os, shutil
from os import system, name
  
def clear():
    # for windows 'nt' else for unix
    system('cls') if name == 'nt' else system('clear')

def change_database_location():
    database_location = Path.cwd() / 'bin/scrapping/'
    source = os.path.join(database_location, "movies.db")
    destination = Path.cwd() / 'data/'
    shutil.move(source, destination)
