import requests
from bs4 import BeautifulSoup
import csv
import os
from random import randint
from time import sleep

url = 'https://www.thewatchcartoononline.tv/dubbed-anime-list'

r = requests.get(url, timeout=(10, 20))
soup = BeautifulSoup(r.content, 'html.parser')


#Check if file exists and if it does delete it
try:
    os.remove("all_href.csv")
except:
    pass

try:
    os.remove("all_episodes_href.csv")
except:
    pass

#Writer one - open first csv in append mode
csvfile_all_href = open('all_href.csv', 'a', newline='')
csvwriter_all_href = csv.writer(csvfile_all_href)

#Find all links
find_all_href = soup.find_all('a', href=True)

all_href_list = []

#Check url's keep good one's and add to list 
for a in find_all_href:
    a = a['href']
    if 'https://www.thewatchcartoononline.tv/anime/' in a:
        all_href_list.append(a)
        #Write to file
        csvwriter_all_href.writerow([a])


all_episodes_href = []

#Writer two - open first csv in append mode
csvfile_all_episodes_href = open('all_episodes_href.csv', 'a', newline='')
csvwriter_all_episodes_href = csv.writer(csvfile_all_episodes_href)


#Go into eah link from all_href_list and take individual episode links
for a in all_href_list:
    a = a
    r = requests.get(a, timeout=(80.7, 99.9))
    soup = BeautifulSoup(r.content, 'html.parser')
    
    div = soup.find("div", { "id" : "sidebar_right3"}).div.a['href']
    print('one_linkdone')
    all_episodes_href.append(div)
    #Write to file a is for grouping anime and div will be diffrent for same anime
    csvwriter_all_episodes_href.writerows([a, div])
    print([a, div])

    sleep_time = randint(10,30)
    print(sleep_time)
    sleep(sleep_time)

print(len(all_episodes_href))