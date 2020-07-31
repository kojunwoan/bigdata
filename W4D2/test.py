balance = 1000
money = 500
msg = ""
with open("./W4D2/bank.log",'r') as file:
    msg = file.read()
print(msg)
with open("./W4D2/bank.log",'w') as file:
    from time import ctime
    file.write(msg + "\n" + ctime() + str(money) + str(balance))