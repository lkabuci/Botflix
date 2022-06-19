from rich.console import Console
from simple_term_menu import TerminalMenu

from helper.utils import set_player
from stream_cli.api.leet import leet
from stream_cli.api.torrentgalaxy import torrent_galaxy
from stream_cli.runner import apprun

console = Console()


def get_top(choice):
    choices = {
        1: apprun(torrent_galaxy()),
        2: apprun(leet()),
    }
    return choices[choice]


def get_movie(choice):
    choices = {
        1: apprun(torrent_galaxy("movie")),
        2: apprun(leet("movie")),
    }
    return choices[choice]


def get_serie(choice):
    choices = {1: apprun(torrent_galaxy("serie")), 2: apprun(leet("serie"))}
    return choices[choice]


def main():
    main_menu_title = " Stream-CLI\n"
    main_menu_items = [
        "Top movies",
        "Search for a movie",
        "Search for a TvSerie",
        "Configuration",
        "Quit",
    ]
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

    config_title = " Choose a default player: \n"
    config_items = ["Back to Main Menu", "VLC", "MPV"]
    config_back = False
    config = TerminalMenu(
        config_items,
        title=config_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    host = ["Back to main menu", "TGx", "1337x", "YTS"]
    host_back = False
    choose_host = TerminalMenu(
        menu_entries=host,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    while not main_menu_exit:
        main_sel = main_menu.show()

        # Top Movies
        if main_sel == 0:
            while not host_back:
                hosts = choose_host.show()
                if hosts == 0:
                    host_back = True
                else:
                    get_top(hosts)
            host_back = False

        # Search By a movies
        elif main_sel == 1:
            while not host_back:
                hosts = choose_host.show()
                if hosts == 0:
                    host_back = True
                else:
                    get_movie(hosts)
            host_back = False

        # Search By TvShows
        elif main_sel == 2:
            while not host_back:
                hosts = choose_host.show()
                if hosts == 0:
                    host_back = True
                else:
                    get_serie(hosts)
            host_back = False

        # Configuration
        elif main_sel == 3:
            while not config_back:
                edit_sel = config.show()
                if edit_sel == 0:
                    config_back = True
                elif edit_sel == 1:
                    set_player("vlc")
                    config_back = True
                elif edit_sel == 2:
                    set_player("mpv")
                    config_back = True
            config_back = False

        # Quit
        elif main_sel == 4:
            main_menu_exit = True


if __name__ == "__main__":
    main()
