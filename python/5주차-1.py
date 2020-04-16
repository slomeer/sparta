# requests, bs4 import
import requests
from bs4 import BeautifulSoup

# url
url = 'https://platum.kr/archives/120958'

# headers : user-agent : 브라우저를 이용해서 접속한 척 하는 것
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 주소로 get 접속해서 받아온 내용을 데이터에 저장
data = requests.get(url,headers=headers)

# bs4로 해당내용을 분석해서 soup에 저장
soup = BeautifulSoup(data.text, 'html.parser')

og_image = soup.select_one('meta[property="og:image"]')
og_title = soup.select_one('meta[property="og:title"]')
og_description = soup.select_one('meta[property="og:description"]')

print(og_image)
print(og_title)
print(og_description)

url_image = og_image['content']
url_title = og_title['content']
url_description = og_description['content']

print(url_image)
print(url_title)
print(url_description)