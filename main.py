from src.fetch_data import *
from src.stream import *
from src.player import *

result = search()
html_content = result[0]
lenght = result[1]
sizes = result[2]
magnets = result[3]

titles = get_titles(html_content, sizes)
magnet = get_magnet_links(magnets)

data = use_same_lenght(titles, sizes)
table = table_it(data)
print(table)



player = check_player()
link = selection(magnet)
stream(magnet=link, default_player=player)