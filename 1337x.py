import asyncio
import httpx
from bs4 import BeautifulSoup

base_url = "https://1337x.to"


async def parse_movie(movie):
    title_and_link = movie.find('td', class_='coll-1 name').find_all('a')
    link = base_url + title_and_link[1]['href']
    async with httpx.AsyncClient() as client:
        response = await client.get(link)
        subsoup = BeautifulSoup(response.content, 'html.parser')
        magnet = subsoup.find('a', href=lambda href: href and href.startswith('magnet'))

        movie_data = {
            'title': title_and_link[1].string,
            'magnet': magnet['href'],
        }
        return movie_data


async def parse_movies(movie_name):
    url = f"https://1337x.to/sort-search/{movie_name}/seeders/desc/1/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        movies = soup.find('tbody').find_all('tr')

        tasks = []
        for movie in movies:
            task = asyncio.create_task(parse_movie(movie))
            tasks.append(task)

        return await asyncio.gather(*tasks)


async def main():
    movie_name = "red notice"
    torrent_1337x_movies = await parse_movies(movie_name)

    for movie in torrent_1337x_movies:
        print(movie)


asyncio.run(main())
