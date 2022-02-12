import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable


def search():
    '''takes no argument return html code'''

    search = input("What are you searching for? ").split(" ")
    search = "+".join(search)

    url = f"https://torrentgalaxy.to/torrents.php?search={search}&sort=seeders&order=desc"

    try:
        response = requests.get(url).text

    except requests.exceptions.RequestException:
        print(
            "\033[91mUnable to connect to torrent provider. Please use vpn. Exiting...\033[0m")
        raise SystemExit(0)

    soup = BeautifulSoup(response, 'html.parser')
    size = soup.find_all("span", class_="badge badge-secondary")
    sizes = [item.text for item in size]
    magnets = soup.find_all("a")
    lenght = len(sizes)

    return (soup, lenght, sizes, magnets)


def get_titles(soup, size):
    title = []
    for i in range(2, len(size)+2):
        temp = soup.select(
            f"div.tgxtablerow:nth-child({i}) > div:nth-child(4) > div:nth-child(1) > a:nth-child(1) > b:nth-child(1)")
        if temp != []:
            for i in temp:
                i = str(i)
                removal_list = ["<b>", "</b>"]
                edit_string_as_list = i.split("<b>")
                final_list = [
                    word for word in edit_string_as_list if word not in removal_list]
                i = ' '.join(final_list)
                edit_string_as_list = i.split("</b>")
                final_list = [
                    word for word in edit_string_as_list if word not in removal_list]
                i = ' '.join(final_list)
                title.append(i)
    return title


def get_magnet_links(magnets):
    '''this function search for the magnet links'''
    magnet = []
    for item in magnets:
        link = item.get('href')
        if "magnet" in str(link):
            magnet.append(link)
    return magnet


def use_same_lenght(title, size):
    diff = len(title) - len(size)
    if diff > 0:
        title = title[:-diff]
    elif diff < 0:
        size = size[:diff]
    data = {
        "Title": title,
        "size": size,
    }
    return data


def table_it(data):
    df = PrettyTable()
    number = [item for item in range(len(data["size"]))]
    df.add_column("Number", number)
    df.add_column("Title", data["Title"])
    df.align["Title"] = "l"
    df.add_column("Size", data["size"])
    return df
