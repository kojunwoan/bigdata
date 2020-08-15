#pip install bs4
#pip install lxml
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
url = "https://comic.naver.com/webtoon/list.nhn?titleId=20853"

res = requests.get(url)
res.raise_for_status()
res.close()
soup = bs(res.text, 'lxml')  # 매개변수를 lxml로 해석...

[print(td.a.get_text()) for td in soup.find_all("td", attrs={"class", "title"})]