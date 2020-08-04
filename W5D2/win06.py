# CPU
# Thread : 하나의 프로세스 내에서 진행되는 하나의 실행 단위를 의미
# MultiThread 

# 프로세서 : 메모장, 워드, 카톡 등등
# 멀티스레드 : 카톡 : 채팅+파일전송
# 파이썬에서 멀티스레드 구현 방법
'''
1. 스레드가 실행할 함수 혹은 메서드를 작성하는 방식
2. threading.Thread 로부터 파생된 파생클래스를 작성하여 사용하는 방식
'''

import threading

def run(who):
    for i in range(1,100):
        print(str(i),"미터 달리는중",who)
run("번개")
run("천둥")
#멀티 스레드 처리
T1 = threading.Thread(target=run, args=("번개",))
T2 = threading.Thread(target=run, args=("천둥",))

#start(): 스레드 동작함수

T1.start()
T2.start()

print("main Thread end......")