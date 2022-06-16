import time

from simple_term_menu import TerminalMenu

def choose_category(terminal, category: str):
    while not terminal_exit:
        category = terminal.show()
        if category == 1:
            return "top"
        elif category == 2:
            return "movie"
        elif category == 3:
            return "serie"
        elif category == 4:
            print("Have a nice day")
            exit(1)


def set_provider(provider: str, category: str):
    if provider == "tgx" and category == "top":
        print("You choose")
        time.sleep(5)
        return
    elif provider == "leet":
        return
    elif provider == "yts":
        return


def main():
    main_menu_title = " Stream-CLI\n"
    main_menu_items = ["TGX", "LEET", "YTS", "Piratebay", "Configuration", "Quit"]
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_exit = False

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        title=main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    edit_menu_title = " Configuration: \n"
    edit_menu_items = ["Edit Config", "Back to Main Menu"]
    edit_menu_back = False
    edit_menu = TerminalMenu(
        edit_menu_items,
        title=edit_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    categories = ["List the top movies", "Search for a movie", "Search fir a TvSerie", "Quit"]
    categories_exit = False
    choose_category = TerminalMenu(
        menu_entries = categories,
        menu_cursor = main_menu_cursor,
        menu_cursor_style = main_menu_cursor_style,
        cycle_cursor = True,
        clear_screen = True
    )    

    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 4:
            while not edit_menu_back:
                edit_sel = edit_menu.show()
                if edit_sel == 0:
                    print("Edit Config Selected")
                    time.sleep(2)
                elif edit_sel == 1:
                    edit_menu_back = True
                    print("Back Selected")
            edit_menu_back = False

        elif main_sel == 0:
            while not categories_exit:
                choose_category("tgx")

        elif main_sel == 1:
            while not categories_exit:
                choose_category("leet")

        elif main_sel == 2:
            while not categories_exit:
                choose_category("yts")

        elif main_sel == 3:
            print("Edit")

        elif main_sel == 5:
            main_menu_exit = True
            print("GoodBye")

if __name__ == "__main__":
    main()



# from typing import Optional
# from stream_cli.api.torrentgalaxy import torrent_galaxy

# from helper.utils import PLAYERS_LIST
# from helper import utils
# from stream_cli.runner import apprun

# import typer
# from rich import print
# from rich import console

# from pathlib import Path


# app = typer.Typer()
# console = console.Console()


# @app.command(short_help="get table of top movies")
# # def main(name: str = typer.Argument("Wade Wilson")):
# def top(source: Optional[str] = typer.Argument("tgx"), limit: Optional[str] = 10):
#     source = source.lower()
#     if source == "tgx":
#         apprun(torrent_galaxy(), True)


# @app.command(short_help="search for a specific movie")
# def search(name: str):
#     apprun(MoviesSpider(name), is_top_movies_choice=False)


# @app.command(short_help="search for a specific TVSerie")
# def serie(name: str):
#     apprun(SeriesSpider(name), is_top_movies_choice=False)


# @app.command
# def config(player: str = typer.Option("mpv", help="set the default player")):
#     player = player.lower()
#     if player not in PLAYERS_LIST:
#         utils.wrong_player(player)
#     else:
#         directory = Path("config/")
#         if not directory.exists():
#             directory.mkdir()
#         with open("config/player.txt", "w") as file:
#             file.write(player)

#         print(f'[bold green]Now "{player}" is your default media player!')

# if __name__ == "__main__":
#     if utils.is_player_valid():
#         app()
#     else:
#         print("[red]Something went wrong, try python3 main.py config 'default_player'[red]")
#         exit(1)
