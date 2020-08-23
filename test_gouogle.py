
from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.webdriver.common.keys import Keys
import time

class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUp(cls):
        print('Start test')
        cls.driver = webdriver.Chrome(".\SeleniumDrivers\chromedriver.exe")
        cls.driver.get('https://google.com')
        time.sleep(2)


    def test_01(self):
        print('Python search')
        driver=self.driver
        input_field = driver.find_element_by_name('q')
        input_field.send_keys('python')
        input_field.send_keys(Keys.ENTER)
        time.sleep(2)

    def test_02(self):
        print('Test Automation search')
        driver=self.driver
        input_field = driver.find_element_by_name('q')
        input_field.send_keys('test automation')
        input_field.send_keys(Keys.ENTER)
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('Test passed')

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/trybak/PycharmProjects/TrainingDev/Report'))