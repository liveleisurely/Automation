import datetime as dt
import pandas as pd
import requests
import time
import urllib.request
import re
import os

from bs4 import BeautifulSoup
from pandas import DataFrame
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import selenium

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# def get_package_version():
#     # datetime은 표준 라이브러리이므로 버전 정보가 없습니다.
#     print("datetime: 표준 라이브러리, 별도의 버전 정보 없음")
    
#     # pandas 버전 정보
#     print(f"pandas: {pd.__version__}")
    
#     # requests 버전 정보
#     print(f"requests: {requests.__version__}")
    
#     # urllib는 표준 라이브러리의 일부이므로 별도의 버전 정보가 없습니다.
#     print("urllib: 표준 라이브러리, 별도의 버전 정보 없음")
    
#     # re는 표준 라이브러리의 일부이므로 별도의 버전 정보가 없습니다.
#     print("re: 표준 라이브러리, 별도의 버전 정보 없음")
    
#     # os는 표준 라이브러리의 일부이므로 별도의 버전 정보가 없습니다.
#     print("os: 표준 라이브러리, 별도의 버전 정보 없음")
    
#     # selenium 버전 정보
#     print(f"selenium: {selenium.__version__}")
    
#     # BeautifulSoup와 ChromeDriverManager는 버전 정보를 다르게 처리할 수 있습니다.
#     # BeautifulSoup 버전 정보를 확인하는 공식적인 방법은 없으나, 패키지 정보에서 확인할 수 있습니다.
#     try:
#         from bs4 import __version__ as bs4_version
#         print(f"BeautifulSoup: {bs4_version}")
#     except ImportError:
#         print("BeautifulSoup 버전 정보를 찾을 수 없습니다.")
    
#     # webdriver_manager의 경우, 버전 정보를 직접적으로 확인하는 방법이 없을 수 있으므로,
#     # 개인 크롬 버전 버전 122.0.6261.112(공식 빌드) (64비트)
#     print("webdriver_manager: 버전 122.0.6261.112(공식 빌드) (64비트)")

# get_package_version()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=헬스케어" 
driver.get(url)
time.sleep(0.5)

driver.execute_script("window.open('', '_blank');")
new_tab_handle = driver.window_handles[-1]
url2 = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=핀테크"
driver.switch_to.window(new_tab_handle)
driver.get(url2)

while True:
    pass


