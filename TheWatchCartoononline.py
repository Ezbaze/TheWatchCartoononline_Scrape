#! /usr/bin/env C:\\Users\\rybit\\anaconda3\\python.exe

import requests
from bs4 import BeautifulSoup
import os

base_url = "https://www.wcofun.com/"
anime_list_url = f'{base_url}dubbed-anime-list'

headers = {
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.72 Safari/537.36'
}

r = requests.get(anime_list_url, timeout=(3.05, 20)).text
soup = BeautifulSoup(r, 'html.parser')

print(soup)

anime_list_container = soup.find('div', {'class': 'ddmcc'})
print(anime_list_container)
all_href = anime_list_container.find_all('a', href=True)

href_list = []
print(f"HREF LIST {len(href_list)}")

for a in all_href:
    if f'{base_url}anime/' in a['href']:
        href_list.append(a['href'])
print('Urls to go through: ' + str(len(href_list)))

try:
    os.mkdir(os.path.join(os.getcwd(), 'images'))
except:
    pass
os.chdir(os.path.join(os.getcwd(), 'images'))

total_to_do = len(href_list)

for a in href_list:
    r = requests.get(a, timeout=(3.05, 20))
    soup = BeautifulSoup(r.content, 'html.parser')

    images = soup.find_all('img')

    for image in images:
        if 'cdn' in image['src']:
            print('----DOING IMAGE ' + str(href_list.index(a)) + '/' + str(total_to_do) +
                  ' left to do ' + str(total_to_do - href_list.index(a)) + ' ----')
            link = 'https:' + image['src']
            print('Got image Link: ' + link)
            name = a.replace('https://www.thewatchcartoononline.tv/anime/', '')
            print('Got image Name: ' + name)
            with open(name + '.jpg', 'wb') as f:
                print('sending request for Image...')
                im = requests.get(link)
                print('Image request SUCCESS!')
                f.write(im.content)
                print('Image SAVED')

print('DONE!!!')
