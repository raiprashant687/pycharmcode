import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

so = Service("C:/Users/prashant/Downloads/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=so)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("to")
time.sleep(4)
step1 = driver.find_elements(By.XPATH,"//div[@class='products']/div")
for steps in step1:
    steps.find_element(By.XPATH,"div/button").click()
time.sleep(5)
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[text()='Apply']").click()
time.sleep(8)
m = driver.find_element(By.CSS_SELECTOR,"span[class='promoInfo']").text
print(m)
assert m == "Code applied ..!"
driver.find_element(By.XPATH,"//div[@class='products']/div/button").click()
