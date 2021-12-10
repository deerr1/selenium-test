
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


class SearchThreeSelectors(unittest.TestCase):

    def setUp(self):
        chrome_driver = '../chromedriver.exe'
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.get("https://www.saucedemo.com/")

    def test_try_login_without_username(self):
        batton = self.driver.find_element_by_name('login-button')
        batton.click()
        block  = self.driver.find_element_by_xpath("//h3[@data-test='error']")
        time.sleep(3)
        assert block.text == 'Epic sadface: Username is required'

    def test_try_login_without_password(self):
        username = self.driver.find_element_by_id('user-name')
        username.send_keys('Test_username')
        batton = self.driver.find_element_by_name('login-button')
        batton.click()
        block  = self.driver.find_element_by_xpath("//h3[@data-test='error']")
        time.sleep(3)
        assert block.text == 'Epic sadface: Password is required'

    def test_try_login_with_not_registered_user(self):
        username = self.driver.find_element_by_id('user-name')
        username.send_keys('Test_username')
        username = self.driver.find_element_by_id('password')
        username.send_keys('Test_user_password')
        batton = self.driver.find_element_by_name('login-button')
        batton.click()
        block  = self.driver.find_element_by_xpath("//h3[@data-test='error']")
        time.sleep(3)
        assert block.text == 'Epic sadface: Username and password do not match any user in this service'

    def test_try_login_with_locked_user(self):
        username = self.driver.find_element_by_id('user-name')
        username.send_keys('locked_out_user')
        username = self.driver.find_element_by_id('password')
        username.send_keys('secret_sauce')
        batton = self.driver.find_element_by_name('login-button')
        batton.click()
        block  = self.driver.find_element_by_xpath("//h3[@data-test='error']")
        time.sleep(3)
        assert block.text == 'Epic sadface: Sorry, this user has been locked out.'

    def test_try_login_with_registered_user(self):
        username = self.driver.find_element_by_id('user-name')
        username.send_keys('standard_user')
        username = self.driver.find_element_by_id('password')
        username.send_keys('secret_sauce')
        batton = self.driver.find_element_by_name('login-button')
        batton.click()
        block  = self.driver.find_element_by_xpath("//h3[@data-test='error']")
        time.sleep(3)
        wait = WebDriverWait(self.driver, 5)
        wait.until(lambda driver: driver.current_url == 'https://www.saucedemo.com/inventory.html')

if __name__ == '__main__':
    unittest.main()
