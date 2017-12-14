import requests
from bs4 import BeautifulSoup
import time
import urllib.request

next_urls =['http://inu-xcorps.ideaboom.net']
visited_urls=[]
while True:
    next_url = next_urls.pop()
    if next_url in visited_urls :
        continue
    print('visit on' +next_url)
    doc = requests.get(next_url)
    soup = BeautifulSoup(doc.text , 'lxml')
    block= soup.select('a')
    for a in block:
        if a.get('href') and a.get('href')[0 : 7] == 'http://':
            print('append on list - ' +a.get('href'))
            if next_url not in visited_urls:
                visited_urls.append(a.get('href')[7:].split('/')[0])
                print('현재 방문했던 urls들' , visited_urls)
            #if a.get('href')[7:].split('/')[0] not in visited_urls:
            next_urls.insert(0,a.get('href'))
            #doc.requests.get()
            #break
