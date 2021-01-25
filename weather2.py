from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=156'
    res = requests.get(url)
    if res.status_code != 200:
        print('error!')
        exit()

    soup = BeautifulSoup(res.text, 'html.parser')
    locations = soup.select('location')
    output = ''
    output += '<h1>광주/전남 중기예보</h1>'
    for location in locations:
        output += '<h2>{}</h2>'.format(location.select_one('city').string)
        output += '<p>날씨 : {}</p>'.format(location.select_one('wf').string)
        output += '<p>최저기온 : {}</p>'.format(location.select_one('tmn').string)
        output += '<p>최고기온 : {}</p>'.format(location.select_one('tmx').string)
    return output

if __name__ == '__main__':
    app.run()