#CSV 파일
# a, b, c = input("3개 받기").split(",")
# print(a,b,c)

print(100,200,300, sep=", ")

print("Hello","Python","World", sep=" ")
print("Hello","Python","World", sep="\t")
print("Hello","Python","World", sep="\n")\

print("오늘은", end="\t")
print("수요일", end=",")
print("내일은", end="\t")
print("목요일")

# y m d h m s 변수를 선언하고 값을 대인한후 아래처럼 출력
#2020/7/15 18:00:00
year = 2020
month = 7
day = 15
hour = 17
minute = 29
second = 30

print(year, month, day, sep="/", end=" ")
print(hour, minute, second, sep=":")
