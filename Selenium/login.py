import time

import timer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

so = Service("C:/Users/prashant/Downloads/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=so)
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"a[class='forgot-password-link']").click()
driver.find_element(By.CSS_SELECTOR,"input[formcontrolname='userEmail']").send_keys("coolrai39@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[formcontrolname='userPassword']").send_keys("Welcome@6rs")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Welcome@6rs")
txt = driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(4)