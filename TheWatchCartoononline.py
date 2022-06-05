import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.thewatchcartoononline.tv/dubbed-anime-list'

headers = {
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

r = requests.get(url, timeout=(3.05, 20))
soup = BeautifulSoup(r.content, 'html.parser')

all_href = soup.find_all('a', href=True)
print('Finding all URLs')

href_list = []
print('href_list READY')

for a in all_href:
    if 'https://www.thewatchcartoononline.tv/anime/' in a['href']:
        href_list.append(a['href'])
print('Urls to go through: '+ str(len(href_list)))

# test_link = 'https://www.thewatchcartoononline.tv/anime/highschool-of-the-dead'

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
            print('----DOING IMAGE ' + str(href_list.index(a)) + '/' + str(total_to_do) + ' left to do ' + str(total_to_do - href_list.index(a)) + ' ----')
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
