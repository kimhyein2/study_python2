import requests
from bs4 import BeautifulSoup
for i in range(941,947):
    url = f'https://search.naver.com/search.naver?sm=tab_drt&where=nexearch&query={i}회로또'
    res = requests.get(url)
    if res.status_code != 200:
        print('접속이 원할하지 않습니다.')
        exit()

    soup = BeautifulSoup(res.text, 'html.parser')
    lotto_numbers = soup.select('.num_box > span')
    # print(lotto_numbers, type(lotto_numbers))
    data = []
    for number in lotto_numbers:
        print(number.text, end=' ')
        f = open('naver-lotto.txt', 'w', encoding='utf-8')
        data.append(number.text)
        f.write(str(data))
        f.close()
    print()
# print(soup, type(soup))
# print(soup)
