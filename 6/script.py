from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path = '../chromedriver.exe', options=options)
    driver.get("https://yandex.ru/")

    elem_1 = driver.find_element_by_id('text')
    elem_1.click()
    elem_1.send_keys("Собаки")
    elem_1.send_keys(Keys.ENTER)
    time.sleep(2)

    elem_2 = driver.find_element_by_name('text')
    elem_2.clear()
    elem_2.send_keys("Кошки")
    elem_2.send_keys(Keys.ENTER)
    time.sleep(2)

    elem_3 = driver.find_element_by_xpath("//input[@aria-label='Запрос']")
    elem_3.clear()
    elem_3.send_keys("Черепаха")
    elem_3.send_keys(Keys.ENTER)

    time.sleep(5)
    driver.close()