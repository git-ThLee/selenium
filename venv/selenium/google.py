# 출처 : 피너트의 게임&일상 블로그
# 개발자 블로그 : https://game1ife-pnut.tistory.com/
# 수정, 2차 배포는 가능하지만, 판매는 금지합니다.

# 필요한 파이썬 패키지
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import os

#사용자가 입력할 단어 ( 차례대로 폴더 이름 / 검색어 )
folder = input('사진을 저장할 폴더 이름을 지정해주세요 : ')
search = input('찾는 사진의 검색어를 지정해주세요 : ')

#폴더 만들기
if not os.path.isdir(folder):
    os.mkdir(folder)

#구글 실행 - 검색하기
driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl")
google_image_search = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
google_image_search.send_keys(search)
google_image_search.send_keys(Keys.RETURN)

# #구글 실행 - 스크롤 최대로 내리기
# SCROLL_PAUSE_SEC = 1.5
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(SCROLL_PAUSE_SEC)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         try:
#             driver.find_element_by_css_selector(".mye4qd").click()
#         except:
#             break
#     last_height = new_height

#구글 실행 - 파일에다가 사진 저장 (기본값 : .png)
google_image = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in google_image:
    try:
        image.click()
        time.sleep(2)
        google_image_url = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.urlretrieve(google_image_url, f'./' + folder + '/' + search + " " + str(count) + ".png")
        count = count + 1
    except:
        pass

#구글 실행 - 종료
driver.close()