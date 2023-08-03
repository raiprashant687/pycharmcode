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
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"a[routerlink='/auth/register']").click()
driver.find_element(By.CSS_SELECTOR,"#firstName").send_keys("prashant")
driver.find_element(By.CSS_SELECTOR,"#lastName").send_keys("rai")
driver.find_element(By.CSS_SELECTOR,"#userEmail").send_keys("raiprashant687@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#userMobile").send_keys("7053334741")
ele= Select(driver.find_element(By.CSS_SELECTOR,"select[formcontrolname='occupation']"))
ele.select_by_index(2)
driver.find_element(By.CSS_SELECTOR,"input[formcontrolname='gender']").click()
driver.find_element(By.CSS_SELECTOR,"#userPassword").send_keys("prashantrai@123")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("prashantrai@123")
driver.find_element(By.CSS_SELECTOR,"#login").click()
time.sleep(2)
txt = driver.find_element(By.CSS_SELECTOR,"h1[class='headcolor']").text
assert txt == 'Account Created Successfully'