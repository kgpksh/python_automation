from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import io
from time import sleep
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


options = ChromeOptions()
options.add_experimental_option("detach", True) # 브라우저 켜지자마자 꺼지는 거 방지
options.headless = True # 실제 눈에 보이는 브라우저 창 열지 않게 하기
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try :
    # get 요청 후 페이지 로딩 될 때까지 기다리기
    browser.get('https://comic.naver.com/webtoon')
    WebDriverWait(browser, 10)

    # 스크롤을 더 못내릴 때 까지 끝까지 내리기
    prev_height = browser.execute_script('return document.body.scrollHeight')
    while True :
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        sleep(2)
        curr_height = browser.execute_script('return document.body.scrollHeight')

        if prev_height == curr_height :
            break
        prev_height = curr_height

    elem = browser.find_element(By.XPATH, "//*[contains(text(),'월요웹툰')]")
    print(elem.text)
    
finally :
    # BeautifulSoup로 페이지 내 소스코드 출력
    soup = BeautifulSoup(browser.page_source, 'lxml')
    print(soup.prettify())

    try :
        detected_value = browser.find_element(By.ID, 'detected_value')
        print(detected_value)
    except :
        print('detected_value 없음')
    # 브라우저 종료
    browser.quit()