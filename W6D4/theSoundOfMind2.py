#pip install bs4
#pip install lxml
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
from pathlib import Path

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
url = "https://comic.naver.com/webtoon/detail.nhn?titleId=20853&no=1237&weekday=tue"

res = requests.get(url)
res.raise_for_status()
res.close()
soup = bs(res.text, 'lxml')  # 매개변수를 lxml로 해석...


# data = soup.find("div", attrs={"class", "wt_viewer"})

# images = data.findAll("img")
# for img in images:
#     path = img['src']
#     res2 = requests.get(path, headers=headers)
#     print(res2)

path = [img['src'] for img in soup.find("div", attrs={"class", "wt_viewer"}).findAll("img")]
for img in path:
    res2 = requests.get(img, headers=headers)
    Path("./img/"+img[46:50]).mkdir(parents=True, exist_ok=True)
    with open("./img/"+img[46:50]+'/'+img[-12:],'wb') as f:
        f.write(res2.content)