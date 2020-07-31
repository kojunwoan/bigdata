#2중 리스트
a=[1,2,3]
b= [10,a,True,"문자열"]

print(b[1])

c=[[1,2],[3,4,5],[6,7,8,9]]
print(c[1][1])
print(c[2][2])


#리스트의 삽입 삭제 연산하기
pet = ['강아지','고양이','거북이','고슴도치']
print(pet)
pet.append("열대어")
print(pet)
pet.insert(0,"이구아나")
print(pet)
pet.extend(["토끼","햄스터"])
print(pet)
pet += ["돼지"]
print(pet)

print(len(pet))

pet.remove("거북이")
print(pet)
del pet[3]
print(pet)

animal = pet
pet[0] = '댕댕이'
print("animal : ", animal)
print("pet : ", pet)
print(id(animal), id(pet))