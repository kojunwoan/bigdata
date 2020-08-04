#현재 작업중인 디렉토리 경로를 얻어오기

import os

print(os.listdir())
print(os.getcwd())


#파일 입출력
#open("파일명","모드")
file = open("./W4D1/hello.txt",'r')
print(file)
print(file.read())
file.close()

file2 = open("./W4D1/hello2.txt",'w')
print(file2)
file2.write("금요일 같은 월요일... 월요병   ")
file2.close()