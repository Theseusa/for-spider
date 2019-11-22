import csv
import requests
import json
url = "https://movie.douban.com/j/chart/top_list?"
headers = {"User-Agent": "Mozilla/5.0"}


params = {"type":"11",
    "start":"0",
    "limit":"20",
    "interval_id":"100:90",
    "action":""
        }

	
res = requests.get(url,params=params,headers=headers)
res.encoding='utf-8'
html = res.text


html = json.loads(html)

for film in html:
    name = film['title']
    score = film['rating'][0]
    with open('豆瓣电影.csv','a',newline="") as f:
        writer = csv.writer(f)
        L = [name,score]
        writer.writerow(L)
