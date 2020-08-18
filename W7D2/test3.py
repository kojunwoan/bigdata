import pyautogui
import time
pyautogui.moveTo(400,400,1)     #절대위치 x,y,지속시간
pyautogui.moveRel(100,100,3)    #상대위치
pyautogui.click(clicks=2, interval=1)   #클릭 횟수 지정..
pyautogui.doubleClick()         #하지만 더블클릭은 이미 있지....

time.sleep(1)
pyautogui.typewrite('hello')