#사용자로부터 국어 영어 수학 점수를 입력받아 총점과 평균을 출력
kor, eng, mat = input("국어 영어 수학 점수를 입력하세요.").split()
total = int(kor) + int(eng) + int(mat)
avg = total / 3
print(total, avg)