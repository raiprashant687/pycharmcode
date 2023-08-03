import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

so = Service('C:/Users/prashant/Downloads/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=so)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"a[href='https://rahulshettyacademy.com/dropdownsPractise/']").click()
time.sleep(5)
"""this step is very important to transfer the control to the window on which we intend to do action on"""
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH,"//input[@id='autosuggest']").send_keys("fr")
time.sleep(2)
list_values = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']")
for value in list_values:
    if value.text == 'France':
        value.click()
        break
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"select[id='ctl00_mainContent_ddl_originStation1']").click()
time.sleep(3)
