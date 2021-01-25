from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():

    return 'Hello, World!'
@app.route('/home')
def home():
    return 'homepage is not ready!'
if __name__ == '__main__':
    app.run()
# import requests
# from bs4 import BeautifulSoup
#
#
# url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=156'
# res = requests.get(url)
#
# if res.status_code != 200:
#     print('error')
#     exit()
#
# soup = BeautifulSoup(res.text, 'html.parser')
#
# html = soup.select('location')
#
# for row in html:
#     print('지역: ',row.select_one('city').text)
#     print('날짜: ',row.select_one('tmEf').text)
#     print('날씨 예보: ',row.select_one('wf').text)
#     print('최저기온: ',row.select_one('tmn').text)
#     print('최고기온: ',row.select_one('tmx').text)
#     print('강수확률: ',row.select_one('rnSt').text,'%')
#     print('-'*30)
#print(soup)
# print(res.status_code)
# print(res.headers)
