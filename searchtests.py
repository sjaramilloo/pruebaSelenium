import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class SearchTests(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'D:\Users\USUARIO\Desktop\Tec\pruebaSelenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
        
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field= driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('salt shaker')
        search_field.submit

        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[4]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))
    
    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, Value= what)
        except NoSuchElementException as variable:
            return False
        return True
    
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner= HTMLTestRunner(output = 'reportes',report_name = 'hello-world-report'))
  