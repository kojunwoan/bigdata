import time

# help(time.time)

print(time.time())
print(time.ctime(), type(time.ctime()))

print(time.ctime().split()[4], time.ctime().split()[-1])

print(dir(time))
#지금 시간을 1초 단위로 출력
while True:
    time.sleep(1)   #1초 sleep
    print(time.ctime().split(),end="\t")
