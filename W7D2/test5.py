#pip install pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui
from random import randint
import pyperclip

# url = "https://www.google.com/"

# browser.find_element_by_id('gb_70').click() #로그인 버튼 클릭
# idinput = browser.find_element_by_id('identifierId')
# idinput.send_keys("01065653313")
# idinput.send_keys(Keys.ENTER)
# pyautogui.alert("로그인 하고 버튼 눌러주세요")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
url = "http://www.kyonggi.ac.kr/myPage.kgu"
browser = webdriver.Chrome(r"E:\dev\python_workspace\chromedriver.exe",chrome_options=chrome_options)
browser.get(url)

browser.find_element_by_id("idida").send_keys("201215459")
sleep(1)
browser.find_element_by_id("passwd").send_keys("ky785488")
sleep(1)
browser.find_element_by_xpath('//*[@id="HSSOLogin"]/div/div[1]/div[1]/div/input[1]').click()
sleep(2)
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(r"E:\dev\python_workspace\img\ok.PNG")))
sleep(2)
browser.find_element_by_xpath('//*[@id="header"]/div[1]/div[2]/div[1]/ul/li[3]/a').click()
sleep(2)
browser.find_element_by_xpath('//*[@id="top1m2"]/img').click()
sleep(10)
browser.maximize_window()
sleep(1)
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(r"E:\dev\python_workspace\img\write.PNG")))
sleep(1)
pyautogui.typewrite("dagda@hanafos.com")
sleep(1)
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(r"E:\dev\python_workspace\img\title.PNG")))
sleep(1)
pyperclip.copy("행운의 편지")
pyautogui.hotkey('ctrl','v')
sleep(1)
pyautogui.click(1550,584)
sleep(1)
pyperclip.copy("잘만들어졌네요.")
pyautogui.hotkey('ctrl','v')
sleep(1)
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(r"E:\dev\python_workspace\img\send.PNG")))
sleep(600)