#pip install opencv-python
import pyautogui

# pyautogui.screenshot("q1.png",region=(1158,207,51,50))
i = pyautogui.locateOnScreen(r"E:\dev\python_workspace\img\search.PNG")

pyautogui.click(pyautogui.center(i))