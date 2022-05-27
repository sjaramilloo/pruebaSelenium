import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class helloworld(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path = r'D:\Users\USUARIO\Desktop\Tec\pruebaSelenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def tearDown(self):
        self.driver.quit()
    
    if __name__ == '__main__':
        unittest.main(verbosity = 2, testRunner= HTMLTestRunner(output = 'reportes',report_name = 'hello-world-report'))
    