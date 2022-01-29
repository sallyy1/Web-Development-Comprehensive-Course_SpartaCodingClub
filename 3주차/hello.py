import requests
from bs4 import BeautifulSoup

## 몽고DB 추가 설정
from pymongo import MongoClient
import certifi ## 보안 관련 추가 설정

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.6syxk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=ca) ## 보안 관련 추가 설치
db = client.dbsparta


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
####print(soup)

title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
print(title)
print(title['href'])


# 그린 북: #old_content > table > tbody > tr:nth-child(3) > td.title > div > a
# 가버나움: #old_content > table > tbody > tr:nth-child(4) > td.title > div > a

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a = movie.select_one('td.title > div > a')
    #print(a) ## <a href="/movie/bi/mi/basic.naver?code=181700" title="안녕 베일리">안녕 베일리</a>

    if a is not None: # 가끔 나오는 가로선(None)은 제외하고 출력
        #print(a.text)

        title = a.text

        # #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
        rank = movie.select_one('img')['alt']

        # #old_content > table > tbody > tr:nth-child(2) > td.point
        star = movie.select_one('td.point').text
        ####print(rank, title, star)


        ## 몽고 DB 조작 추가
        doc = {
            'title' : title,
            'rank' : rank,
            'star' : star
        }

        db.movies.insert_one(doc)