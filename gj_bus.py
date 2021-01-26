import requests
from bs4 import BeautifulSoup

key = '95wt%2BNbCI39pTP4T7WmlBVJvW22lOa0ZkknBhYCusdAzFMxkHJuAA9zAX%2BH%2FKM4TXOrLGiV9gDg2kIzjqUBstQ%3D%3D'
url = 'http://api.gwangju.go.kr/xml/lineInfo?serviceKey='+key
res = requests.get(url)
if res.status_code != 200:
    print('에러발생')
    exit()
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())
lines = soup.select('line')

for line in lines:
    print('노선번호 : ', line.select_one('line_id').text)
    print('노선이름 : ', line.select_one('line_name').text)
    print('기점 : ', line.select_one('dir_up_name').text)
    print('종점 : ', line.select_one('dir_down_name').text)
    if line.select_one('first_run_time') is not None:
        print('막차시각 : ', line.select_one('last_run_time').text)
    if line.select_one('first_run_time') is not None:
        print('배차간격 : ', line.select_one('run_interval').text)
    if line.select_one('run_time_interval') is not None:
        print('첫차시각 : ', line.select_one('first_run_time').text)
    print('노선종류 : ', line.select_one('line_kind').text)
    print('-'*40)