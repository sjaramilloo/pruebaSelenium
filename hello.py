from lib2to3.pgen2 import driver
from re import search
import time
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('http://www.google.com/')
time.sleep(5)
search_box= driver.find_element(By.NAME,'q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)
driver.quit()