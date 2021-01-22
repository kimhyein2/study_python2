# p.175
import os
import requests
try:
    os.mkdir('images')
except:
    os.chdir('images')

# print(os.getcwd())
url = 'https://pbs.twimg.com/media/EB5Pq3rVUAAYjxI.jpg'
res = requests.get(url)
img = res.raw.read()
# print(res.status_code)
# print(res.headers)
os.chdir('images')
with open('photo.jpg','wb') as f:
    f.write()

'''f = open('lotto.txt', 'w', encoding='utf-8')
 line = f.readline()
 print(line)'''
# lines = f.readlines()
# for line in lines:
#     print(line)
# f = open('lotto.txt', 'a', encoding='utf-8')
# for i in range(11, 20):
#     data = '%d 번째 줄입니다.\n' % i
#     f.write(data)
# f.close()
