./nameOfVirtualEnv/Scripts/activate
./nameOfVirtualEnv/Scripts/deactivate
pip install PyUnitReport
pip install selenium
pip install selenium==4.1.3
pip install PyUnitReport


#Plantilla

import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class nombreDeClase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'D:\Users\USUARIO\Desktop\Tec\pruebaSelenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
         
    def test(self):
        pass

    def tearDown(self):
        return super().tearDown()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes',report_name = 'nombre-del-archivo-report'))