with open("./W4D1/rain.txt", 'r', encoding='utf-8') as file:
    data = file.readlines()
    print(data)

lines = ["안녕하세요\n", "오늘은 금요일\n", "이면 좋겠네요\n"]

with open("./W4D1/msg3.txt", 'w', encoding='utf-8') as file2:
    file2.writelines(lines)