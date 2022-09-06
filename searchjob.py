import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class SearchJob(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'D:\Users\USUARIO\Desktop\Tec\pruebaSelenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://co.talent.com/jobs?")
        

    def test_new_job(self):
        driver = self.driver
        driver.find_element_by_id('nv-k').click()


        type_job = driver.find_element_by_id('nv-k').send_keys('qa')
        submit_button = driver.find_element_by_class_name('button--submit')
        self.driver.implicitly_wait(10)


    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes',report_name = 'register-report'))
     