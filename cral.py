import requests
from bs4 import BeatifulSoup

source = requests.get('http://cafe.naver.com/lfckorea/393197')
soup = BeautifulSoup(source.text.'lxml')
tds=soup.select('tbody'[0]).select('tr')[1].select('td[colspan=5]')
for t in tds:
    print("-"*10)
    print(t.text.strip())
    num=num-1
