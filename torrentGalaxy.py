import asyncio
import bs4.element
import httpx
from bs4 import BeautifulSoup
import sys


async def get_movie_data(movie):
    movie_data = {
        'type': movie.find('small').string,  # Optional
        'title': movie.find('b').string,
        'magnet': movie.find('i', class_='glyphicon glyphicon-magnet').previous_element['href'],
        'size': movie.find('span', class_='badge badge-secondary txlight').string,
        'seeders/leeches': get_seeders_leeches(movie.find('span', title='Seeders/Leechers').find_all('b')),
    }
    return movie_data


async def parse_movies(movie_name):
    movie_name = movie_name.replace(" ", "+")
    params = {'search': movie_name, 'lang': '0', 'nox': '1', 'sort': 'seeders', 'order': 'desc'}

    async with httpx.AsyncClient() as client:
        response = await client.get('https://torrentgalaxy.to/torrents.php', params=params, timeout=60)
        soup = BeautifulSoup(response.text, 'html.parser')
        movies = soup.find_all('div', class_='tgxtablerow txlight')

        tasks = []
        for movie in movies:
            task = asyncio.create_task(get_movie_data(movie))
            tasks.append(task)

        return await asyncio.gather(*tasks)


def get_seeders_leeches(seeds_leeches_content: bs4.element.ResultSet) -> str:
    seeders = seeds_leeches_content[0].string
    leeches = seeds_leeches_content[1].string
    return str(seeders + "/" + leeches)


async def main():
    movie_name = input("Enter the movie name: ")
    torrent_galaxy_movies = await parse_movies(movie_name)

    for movie in torrent_galaxy_movies:
        print(movie)


asyncio.run(main())
