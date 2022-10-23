from argparse import Action
from lib2to3.pgen2 import driver
from operator import imod
from turtle import onclick
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class CreateTest(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("https://hemisferiod.clapdev.com/ClapAdmin/login.xhtml")
        #assert"Google Tranlate" in driver.title
        driver.implicitly_wait(10)
        driver.maximize_window()

    def test_log(self):
        driver = self.driver
        driver.implicitly_wait(10)
        element = driver.find_element(By.ID, "form:j_idt25")
        element.send_keys("sebastian.jaramillo@hemisferiod.co")    
        element = driver.find_element(By.ID, "form:j_idt27")
        element.send_keys("Password123*") 
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        
    def create_less(self):
        driver = self.driver
        element = driver.find_element(By.ID, "j_idt77")
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.click(on_element=element)
        actions.perform()
        time.sleep(5)

    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.close()
  
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes',report_name = 'new-less'))
