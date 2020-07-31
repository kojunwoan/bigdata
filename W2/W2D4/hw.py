k = list(range(1,101))  #1부터 100까지의 값을 요소로 갖는 k리스트 작성
v = k[24:45] # 25~ 45번까지 요소를 잘라와 v리스트 생성
for i in v[::2]: # 반복문 사용하여 홀수번째 요소만 출력
    print(i)
print(k)
print(v)
