from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from pathlib import Path

url = "https://movie.naver.com/movie/running/current.nhn"
res = requests.get(url)
res.raise_for_status()
soup = bs(res.text, 'lxml')
# pprint(soup)
# hrefL = [div.a["href"] for div in divL]
# codeL = [href.split("=")[1] for href in hrefL]
# for href in hrefL:
#     pprint(href.split("=")[1])
dtL = soup.find_all("dt",attrs={"class","tit"})
urlL = {dt.a["href"].split("=")[1]:dt.a.get_text() for dt in dtL}
imgsrcL = []
# pprint(urlL)
for url, name in urlL.items():
    res2 = requests.get("https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode="+url)
    pprint("https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode="+url+"          "+name)
    soup2 = bs(res2.text, "lxml")
    imgsrc = soup2.find("img")['src']
    imgsrcL.append(imgsrc+name)
    # res3 = requests.get(imgsrc)
    # Path("./img/movie_poster").mkdir(parents=True,exist_ok=True)
    # with open("./img/movie_poster/"+name+".jpg",'wb') as f:
    #     f.write(res3.content)
    # idx += 1
    # with open("./img/movie_poster/movie{}.jpg".format(idx),'wb') as f:
    #     f.write(res3.content)
pprint(imgsrcL)