#with open("파일명",파일모드) as 파일객체:
#    코드

# with open("./W4D1/msg.txt",'w') as file:
#     file.write("오늘은 여기까지...\n")

with open("./W4D1/msg.txt",'r') as file2:
    # print(file2.read(), type(file2.read()))
    print(file2.read().split())