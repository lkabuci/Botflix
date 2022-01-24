'''
features to be added:
    the ability to sort items
    load in the second page
    Enter size value
    like grep command
'''


import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import subprocess


def get_titles():
    title = []
    for i in range(2, len(size)+2):
        temp = soup.select(f"div.tgxtablerow:nth-child({i}) > div:nth-child(4) > div:nth-child(1) > a:nth-child(1) > b:nth-child(1)")
        if temp != []:
            for i in temp:
                i = str(i)
                removal_list = ["<b>","</b>"]
                edit_string_as_list = i.split("<b>")
                final_list = [word for word in edit_string_as_list if word not in removal_list]
                i = ' '.join(final_list)
                edit_string_as_list = i.split("</b>")
                final_list = [word for word in edit_string_as_list if word not in removal_list]
                i = ' '.join(final_list)
                title.append(i)
    return title


def get_magnet_links():
    '''this function search for the magnet links'''
    magnet = []
    for item in magnets:
        link = item.get('href')
        if "magnet" in str(link):
            magnet.append(link)
    return magnet



search = input("What are you searching for? ").split(" ")
search = "+".join(search)

url = f"https://torrentgalaxy.to/torrents.php?search={search}&sort=size&order=desc"
response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')

titles = soup.find_all("b", class_="txdark")
sizes = soup.find_all("span", class_="badge badge-secondary")
magnets = soup.find_all("a")


size = [ item.text for item in sizes ]

title = get_titles()
magnet = get_magnet_links()

data = {
    "Title": title,
    "size": size,
}


df = PrettyTable()

number = [item for item in range(len(size))]

df.add_column("Number", number)
df.add_column("Title", title)
df.align["Title"] = "l"
df.add_column("Size", size)
print(df)

def selection(magnet):

    lenght = [item for item in range(len(magnet))]
    is_invalid = True
    # TODO: add a check if the number is valid or not
    
    number = int(input("Enter Your Choice: "))
    
    return magnet[number]

def stream(magnet):
    # TODO: add the ability to check if a vlc or other video player exist
    # supported player
    # DNLA
    # MPlayer
    # MPV
    # OMX
    # VLC
    # IINA
    # SMPlayer
    # XBMC 
    subprocess.run(["webtorrent", magnet, "--mpv"])

stream(selection(magnet))
