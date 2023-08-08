import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

so = Service("C:/Users/prashant/Downloads/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=so)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
radiobuttons = driver.find_elements(By.XPATH,"//input[@type='radio']")
for radio in radiobuttons:
    if radio.get_attribute("value")=="radio3":
        radio.click()
        assert radio.is_selected()

time.sleep(5)