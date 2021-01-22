from urllib import request
import os
# 1. 텍스트 데이터
# res = request.urlopen('https://www.google.co.kr')
# 2. 바이너리 데이터 (아래 주석을 해제!)
res = request.urlopen('https://www.google.co.kr/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')
# 3. 텍스트 데이터 읽어서 변수에 기록
# res_text = res.read()
res_img = res.read()
# 4. 텍스트 데이터 출력
# print(res_text)
path = os.getcwd()
if '/static' not in path:
    os.mkdir('static')
    os.chdir('static')
else:
    os.chdir('static')
with open('google_logo.png', 'wb') as f:
    f.write(res_img)
    print('completed')
'''
예외처리
from urllib import request
import os
# 1. 텍스트 데이터
# res = request.urlopen('https://www.google.co.kr')
# 2. 바이너리 데이터 (아래 주석을 해제!)
res = request.urlopen('https://www.google.co.kr/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')
# 3. 텍스트 데이터 읽어서 변수에 기록
# res_text = res.read()
res_img = res.read()