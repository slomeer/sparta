import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

i = 1
for music in musics:
    musicName = music.select_one('td.info > a.title.ellipsis')
    singer = music.select_one('td.info > a.artist.ellipsis')
    print(i, end=' ')
    print(musicName.text.strip(), end=' ')
    print(singer.text.strip())
    i += 1
