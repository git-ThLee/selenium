# 필요한 파이썬 패키지
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import os

#구글 실행 - 검색하기
driver = webdriver.Chrome()

url = 'https://naver.com'
driver.get(url)

driver.find_element_by_xpath('//*[@id="query"]').send_keys('아이유')
driver.find_element_by_xpath('//*[@id="search_btn"]/span[2]').click()

while(True):

    pass