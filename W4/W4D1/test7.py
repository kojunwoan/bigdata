#���� �۾����� ���丮 ��θ� ������

import os

print(os.listdir())
print(os.getcwd())


#���� �����
#open("���ϸ�","���")
file = open("./W4D1/hello.txt",'r')
print(file)
print(file.read())
file.close()

file2 = open("./W4D1/hello2.txt",'w')
print(file2)
file2.write("�ݿ��� ���� ������... ���亴   ")
file2.close()