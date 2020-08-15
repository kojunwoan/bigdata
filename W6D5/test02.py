#pip install selenium
# #selenium
# 웹 브라우저의 자동화를 가능하게 하는 다양한 도구와 라이브러리 포함하는 프로젝트
#webdriver

#브라우저 버전 확인 | 84.0.4147.125
#chrome://version

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome(r"E:\dev\python_workspace\chromedriver.exe")
browser.get("http://www.naver.com")
element = browser.find_element_by_id("query")
element.click()
element.send_keys("택배 없는 날")
element.send_keys(Keys.ENTER)
time.sleep(3)

browser.get("http://www.google.com")
element = browser.find_element_by_name("q")
element.click()
element.send_keys("광복절")
element.send_keys(Keys.ENTER)
time.sleep(3)
element = browser.find_element_by_name("q")
element.click()
element.send_keys(Keys.BACK_SPACE)
element.send_keys(Keys.BACK_SPACE)
element.send_keys(Keys.BACK_SPACE)
element.send_keys("휴일")
time.sleep(3)
