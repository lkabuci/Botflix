import asyncio

from bs4 import BeautifulSoup
import httpx

base_url = "https://rargb.to"


<<<<<<< HEAD
=======
# r = httpx.get(base_url, timeout=60)
# soup = BeautifulSoup(r, "html.parser")
#

async def parse_movie(movie):
    title_and_link = movie.find('a', href=lambda href: href and href.startswith('/torrent/'))
    link = base_url + title_and_link['href']
    async with httpx.AsyncClient() as client:
        response = await client.get(link)
        subsoup = BeautifulSoup(response.content, "html.parser")
        magnet = subsoup.find('a', href=lambda href: href and href.startswith("magnet:"))

    movie_data = {
        "title": title_and_link.string,
        "magnet": magnet['href']
    }

    return movie_data


async def parse_movies(movie_name):
    params = {"search": movie_name, "order": "seeders", "by": "DESC"}
    url = base_url + "/search/"
    async with httpx.AsyncClient as client:
        response = await client.get(url, params=params)
        soup = BeautifulSoup(response.text, "html.parser")
        movies = soup.find_all('tr', class_="lista2")

        tasks = list()
        for movie in movies:
            task = asyncio.create_task(parse_movie(movie))
            tasks.append(task)

        return await asyncio.gather(*tasks)


async def main():
    movie_name = "red notice"
    rargb_movies = await parse_movies(movie_name)

    for movie in rargb_movies:
        print(movie)


>>>>>>> newApi
def get_magnet(link) -> str:
    subr = httpx.get(link, timeout=60)
    subs = BeautifulSoup(subr.text, 'html.parser')
    return str(subs.find('a', href=lambda href: href and href.startswith('magnet:'))['href'])


movie_name = "red notice"
params = {"search": movie_name, "order": "seeders", "by": "DESC"}
r = httpx.get(base_url + "/search/", params=params, timeout=60)
soup = BeautifulSoup(r.text, "html.parser")
movies = soup.find_all('tr', class_="lista2")


def get_seeders_leechers(movie) -> str:
    seeders = movie[5].find('font').string
    leechers = movie[6].string
    return str(seeders + "/" + leechers)


for movie in movies:
    title_and_link = movie.find('a', href=lambda href: href and href.startswith('/torrent/'))
    all_components = movie.find_all("td", class_="lista")
    movie_data = {
        "title": title_and_link.string,
        "category": all_components[2].contents[0].string,
        "magnet": get_magnet(base_url + title_and_link['href']),
        "seeders/leechers": get_seeders_leechers(all_components),
        "size": all_components[4].string
    }
    print(movie_data)
<<<<<<< HEAD

=======
>>>>>>> newApi
