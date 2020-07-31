import pickle

with open("LOL.dat", 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    addrs = pickle.load(file)
    strength = pickle.load(file)
    intelligence = pickle.load(file)
    money = pickle.load(file)
    exp = pickle.load(file)
    level = pickle.load(file)

print("이름 :", name)
print("나이 :", age)
print("주소 :", addrs)
print("공격력 :", strength)
print("주문력 :", intelligence)
print("돈 :", money)
print("경험치 :", exp)
print("레벨 :", level)