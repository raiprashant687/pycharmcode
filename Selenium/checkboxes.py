import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

so = Service('C:/Users/prashant/Downloads/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=so)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
list_of_checkboxes = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
for checkbox in list_of_checkboxes:
    if checkbox.get_attribute("name")=="checkBoxOption2":
        checkbox.click()
        assert checkbox.is_selected()
        break
time.sleep(5)
