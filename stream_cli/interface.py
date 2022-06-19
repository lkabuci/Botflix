from rich import box
from rich.console import Console
from rich.table import Table


def print_table_of_movies(list_of_movies: list):
    """takes a list of dictionnaries that contain movies data in it
    is_top_movies_choice: wheather searched for top_movies or custom search
    """
    table = Table(title="🎖🎥 Stream-CLI 🎥🎖", box=box.HEAVY)

    table.add_column("Index", justify="center", style="yellow")
    table.add_column("Title", style="white", no_wrap=False)
    table.add_column("Size", justify="center", style="red")
    table.add_column("views", justify="center", style="yellow")
    table.add_column("Seeds", justify="center", style="green")
    table.add_column("Leeches", justify="center", style="red")

    for movie in list_of_movies:
        table.add_row(
            str(movie["index"]),
            movie["title"],
            movie["size"],
            movie["views"],
            movie["seeds"],
            movie["leeches"],
        )

    console = Console()
    console.print(table)
