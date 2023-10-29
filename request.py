from random import *
import requests
from bs4 import BeautifulSoup

def gifs(name):
    url = "https://tenor.com/fr/search/" + name + "-gifs"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    gif = soup.find_all("img")
    a = []
    r = 0
    for gifs in gif:
        a.append(gifs['src'])
        r += 1
    i = randint(3, r)
    return a[int(i)]

def poorn():
    url = "https://www.npns.fr/gif-porno/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    gif = soup.find_all("img")
    a = 0
    b = ""
    while ".gif" not in b:
        gifs = []
        i = 0
        for gifss in gif:
            gifs.append(gifss['src'])
            i += 1
        a = randint(0, i)
        b = gifs[a]
    return b

def hentaii():
    url = "https://www.npns.fr/hentai-gif/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    gif = soup.find_all("img")
    a = 0
    b = ""
    while ".gif" not in b:
        gifs = []
        i = 0
        for gifss in gif:
            gifs.append(gifss['src'])
            i += 1
        a = randint(0, i)
        b = gifs[a]
    return b




