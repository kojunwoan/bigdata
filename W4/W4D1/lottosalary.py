import random

def raise_rnd_salary(sal):
    if random.randint(0,1):
        print("강화성공!!")
        sal *= 1.2
    return int(sal)
    
def reduce_rnd_salary(sal):
    if random.randint(0,1):
        sal *= 0.8
    return int(sal)
    