#pip install bs4
#pip install lxml
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
url = "https://comic.naver.com/webtoon/list.nhn?titleId=20853"

res = requests.get(url)

res.raise_for_status()
# print(res, res.status_code, res.text)
res.close()
# pprint(res.text)
soup = bs(res.text, 'lxml')  # 매개변수를 lxml로 해석...
# print(soup, type(soup))
print(soup.find("a"))  # soup객체에서 처음 발견되는 td엘리먼트를 출력
print(soup.a)
print(soup.a.attrs)
print(soup.a.get_text())
print(soup.a.attrs['href'])
print(soup.find("td", attrs={"class", "title"}))
print(soup.find("td", attrs={"class", "title"}).a.get_text())
