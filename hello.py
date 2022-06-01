from lib2to3.pgen2 import driver
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class Helloworld(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r'D:\Users\USUARIO\Desktop\Tec\pruebaSelenium\chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(4)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_visit_wiki(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner= HTMLTestRunner(output = 'reportes',report_name = 'hello-world-report'))
     