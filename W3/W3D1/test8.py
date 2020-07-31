#자판기

unit = [50000,10000,5000,1000,500,100,50,10,1]
menu = [["보리차",1800],["막걸리",2000],["파전",3000],["스파게티",6000],["산삼",200000000],["돈가츠",8000]]
for i in menu:
    print("{:>6}\t: {}원".format(i[0],i[1]))
money = int(input("지폐를 넣어주세요 : "))

def Changes(money):
    for i in unit:
        a, money = divmod(money,i)
        if a != 0:
            print(str(i)+"원\t:",a,"개")

sel_menu = menu[int(input("번호를 선택하세요 : "))-1]
amount = int(input("수량을 선택하세요 : "))

if money >= sel_menu[1] * amount:
    print(sel_menu[0],"상품을", str(amount)+"개 내보냈어요.")
    money -= sel_menu[1]*amount
    if money>0:
        print("잔돈 : ",money,"원")
    Changes(money)
else:
    print("잔액이 부족하여 반환합니다..\n잔돈",money,"원")
    Changes(money)

    