#pip install bs4
#pip install lxml
import requests
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup as bs
from pprint import pprint
from pathlib import Path

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
urlL = ["https://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=&page="+str(i) for i in range(1,125)]

for url in urlL:
    res = requests.get(url)
    res.raise_for_status()
    res.close()
    soup = bs(res.text, 'lxml')
    
    pageL = ["https://comic.naver.com"+last for last in [td.a.attrs["href"] for td in soup.find_all("td", attrs={"class", "title"})]]
    for page in pageL:
        res2 = requests.get(page, headers=headers)
        soup2 = bs(res2.text, 'lxml')
        path = [img['src'] for img in soup2.find("div", attrs={"class", "wt_viewer"}).findAll("img")]
        for img in path:
            res3 = requests.get(img, headers=headers)
            Path("./img/"+img[46:50]).mkdir(parents=True, exist_ok=True)
            with open("./img/"+img[46:50]+'/'+img[-12:],'wb') as f:
                f.write(res3.content)
            res3.close()
        res2.close()
    # soup = bs(res.text, 'lxml')  # 매개변수를 lxml로 해석...
    # print(soup.find_all("td", attrs={"class", "title"}))
    # # [print(td.a.get_text()) for td in soup.find_all("td", attrs={"class", "title"})]