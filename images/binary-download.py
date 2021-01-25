import os
import requests

url = 'https://pbs.twimg.com/media/EB5Pq3rVUAAYjxI.jpg'
res = requests.get(url)

img = res.content
with open('photo2.jpg','wb') as f:
    f.write(img)