import time

def saveLog(savedir, money, balance, mode):
    if mode:
        type = "출금"
    else:
        type = "입금"
    with open(savedir,'a') as file:
        file.write("{}\t{} : {}\t 잔액 : {}\n".format(time.ctime(),type,money,balance))

def getBalance(savedir):
    with open(savedir,'r') as file:
        print(file.readlines(), type(file.readlines()))
        # return int(file.readlines()[len(file.readlines())].split()[-1:][0])
