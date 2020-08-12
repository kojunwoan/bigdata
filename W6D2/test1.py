#특정 정보를 추출하는 기술 크롤링


import requests

res = requests.get("http://m.naver.com")
#200 : 정상(HTTP.status)
#404 : 페이지를 찾을 수 없음 : url(uniform resource location) 오류
#500 : 서버사이드 로직 에러

# if res.status_code == requests.codes.ok:
#     print("응답코드 200번이닷")
#     print(len(res.text))

res.raise_for_status()  #에러가 있으면 에러 메세지를 출력하고 바로 종료
# print(res.text)
with open("google.html", 'w', encoding='utf-8') as f:
    f.write(res.text)