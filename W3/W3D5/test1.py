keyword = "오늘은 비가 언제 까지 올까요?".split()

print(keyword, type(keyword))

#set Comprehesion
for word in keyword:
    print(len(word))
print({len(word) for word in keyword})
print({len(word) for word in keyword if len(word)>3})

#dictionary Comprehesion
countrys = {"한국":"서울", "일본":"도쿄", "중국":"북경", "UAE":"아부다비"}

for country, capital in countrys.items():
    print(country, capital)
capital = {country : capital for country, capital in countrys.items()}
print(capital)
    


def solution(participant, completion):
    l = dict()
    while True:
        l.
    answer = ''
    return answer