from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

url = "http://www.naver.com"
browser = webdriver.Chrome(r"E:\dev\python_workspace\chromedriver.exe",chrome_options=webdriver.ChromeOptions().add_argument("--incognito"))
browser.get(url)

browser.maximize_window()

search = browser.find_element_by_id('query')
sleep(1)
search.send_keys("종로3가 맛집")
sleep(1)
search.send_keys(Keys.ENTER)
sleep(5)
pyautogui.scroll(-1200)

for i in range(20):
    ulElem = browser.find_element_by_css_selector('#place_main_ct > div > div > div.sc_box.place_list > div.list_area > ul')
    lists = ulElem.find_elements_by_css_selector('.list_item.type_restaurant')  #css에서 class 사용할때..
    for store in lists:
        print(str(i+1), store.find_element_by_css_selector("div.tit > span > a > span").text)
    if not i == 19:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(r"E:\dev\python_workspace\img\next.PNG")))
    # sleep(0.5)
sleep(60)