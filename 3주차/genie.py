import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
####print(soup)

# 1. 순위
# #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number

# 2. 곡 제목
# #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis

# 3. 가수
# #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')  ## (주의!) tr 까지만 select 해줘야 함


for elem in musics:

    if elem is None: ## (방어 코드)
        continue

    # 1번.
    rank_pre = elem.select_one('td.number')
    rank = list(rank_pre.text.strip().split('\n'))
    ####print(rank[0])


    # 2번.
    title_pre = elem.select_one('td.info > a.title.ellipsis')
    ####print(list(title_pre.text.split('\n'))) ## 결과 : ['19금', '                                            ', '                                        ', '                                        ', '                                    ', '                                    Peaches (Feat. Daniel Caesar & Giveon)']

    title_list = list(line.strip() for line in list(title_pre.text.split('\n')))
    ####print(title_list) ## 결과 : ['', '19금', '', '', '', '', 'Peaches (Feat. Daniel Caesar & Giveon)']

    title = title_list[-1]


    # 3번.
    artist_pre = elem.select_one('td.info > a.artist.ellipsis')
    artist = artist_pre.text.strip()
    ####print(artist)


    print(rank[0], title, artist)

