from rich import box
from rich.console import Console
from rich.table import Table


def print_table_of_movies(list_of_movies: list, is_top_movies_choice: bool):
    """takes a list of dictionnaries that contain movies data in it
    is_top_movies_choice: wheather searched for top_movies or custom search
    """
    if is_top_movies_choice:
        table = Table(title="🎖🎥 Top Movies 🎥🎖", box=box.HEAVY)
    else:
        table = Table(title="🔎🎦 Search results 🎦🔍", box=box.HEAVY)

    table.add_column("Index", justify="center", style="yellow")
    table.add_column("Title", style="white", no_wrap=False)
    table.add_column("Size", justify="center", style="red")
    table.add_column("views", justify="center", style="yellow")
    table.add_column("Seeds", justify="center", style="green")

    for movie in list_of_movies:
        table.add_row(
            str(movie["index"]),
            movie["title"],
            movie["size"],
            movie["views"],
            movie["seeds"],
        )

    console = Console()
    console.print(table)
