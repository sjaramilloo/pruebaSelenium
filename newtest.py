from lib2to3.pgen2 import driver
from operator import imod
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 

class NewTest(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("https://translate.google.com.co/?hl=en&tab=wT")
        #assert"Google Tranlate" in driver.title
        driver.implicitly_wait(5)
        driver.maximize_window()

    def test_traductor(self):
        driver = self.driver
        element = driver.find_element(By.CLASS_NAME, "er8xn")
        element.clear()
        element.send_keys("Hola Mundo")
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        print("hola")

    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.close()
  
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes',report_name = 'newTest-report'))
