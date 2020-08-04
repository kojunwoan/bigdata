import os
#운영체제에서 제공되는 여러 기능을 파이썬에서 수행할수 있게 해주는 모듈 : os

print(dir(os))

#현재 작업 디렉토리 검색
print(os.getcwd)
#get 뭔가 줘/ set 뭔가 바꿀거야

print(os.listdir())

print(os.listdir('W4D1'))

print(os.listdir('.'))
# print(os.listdir('..'))                         #상대경로
print(os.listdir('e:\\dev\\python_workspace'))    #절대경로



#현재 작업 디렉토리에 있는 모든 파일을 출력
#반복문을 사용해서 한개씩 출력

for file in os.listdir('c:/'):
    # if file.find('.zip') != -1:
    if file.endswith('zip'):
        print(file)