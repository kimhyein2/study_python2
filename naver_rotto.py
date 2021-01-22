import requests
from bs4 import BeautifulSoup
import time
start = 941
end = 946
for i in range(start, end + 1):
    url = f'https://search.naver.com/search.naver?sm=tab_drt&where=nexearch&query={i}회로또'
    res = requests.get(url)
    if res.status_code != 200:
        print('접속이 원할하지 않습니다.')
        exit()

    soup = BeautifulSoup(res.text, 'html.parser')
    lotto_numbers = soup.select('.num_box > span')
    lotto = []
    for number in lotto_numbers:
       lotto.append(number.text)
       # print(number.text, end=' ')
       # p.171 파일 읽고 쓰기(1)
       #  f = open('lotto.txt','w', encoding='utf-8')
       #  f.write(number.text)
       #  f.close()
       #  p.176~177 with문을 이요해 파일 읽고 쓰기(2)
       # with open('lotto.txt', 'w', encoding='utf-8') as f:
        #     f.write(number.text)
        #
    with open('lotto.txt', 'a' , encoding='utf-8') as f:
        f.write(str(lotto))
        f.write('\n')

    time.sleep(3)
# print(lotto_numbers, type(lotto_numbers))
# print(soup, type(soup))
# print(soup)
