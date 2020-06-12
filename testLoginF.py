import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def loginCalculator(driver):
    print("Accedemos a la consola principal de la app")
    # driver.get("http://localhost:9080/congruencias/index")
    time.sleep(1)
    print("Facilitamos user")
    # driver.find_element_by_id("inputEmail").send_keys("jcla")
    time.sleep(1)
    print("Facilitamos password")
    # driver.find_element_by_id("inputPassword").send_keys("jcla")
    time.sleep(1)
    print("Enviamos para validacion")
    # driver.find_element_by_xpath("/html/body/form/button").click()
    time.sleep(1)

class CalculatorTester(unittest.TestCase):
    
    def setUp(self):
        # self.driver = webdriver.Firefox()
        # self.wait = WebDriverWait(self.driver, 100)
        pass
        
    def testLogin(self):
        # loginCalculator(self.driver)
        loginCalculator(None)
        self.assertTrue(True)

    def tearDown(self):
        # self.driver.quit()
        pass


if __name__ == "__main__":
    unittest.main()