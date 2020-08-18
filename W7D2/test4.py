from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from random import randint

# url = "https://www.google.com/"

# browser.find_element_by_id('gb_70').click() #로그인 버튼 클릭
# idinput = browser.find_element_by_id('identifierId')
# idinput.send_keys("01065653313")
# idinput.send_keys(Keys.ENTER)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
url = "https://www.moakt.com/"
browser = webdriver.Chrome(r"E:\dev\python_workspace\chromedriver.exe",chrome_options=chrome_options)
browser.get(url)

makeMail = browser.find_element_by_class_name("mail_in")
makeMail.click()
makeMail.send_keys("kojun"+str(randint(1,100)))
time.sleep(1)

browser.find_element_by_class_name("mail_butt").click()
time.sleep(2)

browser.find_element_by_class_name("iconic_button").click()
time.sleep(2)

browser.find_element_by_name("mail_to").send_keys("kojunwoan@gmail.com")
browser.find_element_by_name("mail_subject").send_keys("테스트메일이다")
browser.find_element_by_name("mail_text").send_keys("자동발송메일 테스트...")

pyautogui.alert("사람인걸 증명해주세요^^")

browser.find_element_by_class_name("button-blue.submit-button").click()

time.sleep(600000)