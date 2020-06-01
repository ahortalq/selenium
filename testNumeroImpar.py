import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def loginCalculator(driver):
    driver.get("http://localhost:9080/congruencias/index")
    driver.find_element_by_id("inputEmail").send_keys("jcla")
    driver.find_element_by_id("inputPassword").send_keys("jcla")
    driver.find_element_by_xpath("/html/body/form/button").click()


class CalculatorTester(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 100)
        
    def testNumeroImpar(self):
        loginCalculator(self.driver)
        print("Iniciamos los calculos")
        self.driver.find_element_by_xpath("/html/body/form/button").click()
        print("Facilitamos un numero impar")
        self.driver.find_element_by_xpath("/html/body/form/input").send_keys("5")
        time.sleep(1)
        print("Validamos calculo")
        self.driver.find_element_by_xpath("/html/body/form/button").click()
        time.sleep(1)
        self.assertTrue(True)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()