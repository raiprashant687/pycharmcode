#implicit waits waits for the element to be visible rather than blindly waiting for the element i.e
# let say if there is implicitwait of 6 seconds in a script and some element on the same page takes 2
# seconds to be clickable here the implicit wait saves 4 seconds and thereby not waits untill the said time
"""problem with implicit waits is that they cant be applied on the find.elements method of the driver clase
as the expected response is list and in case of failure an empty list is returned"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

so = Service("C:/Users/prashant/Downloads/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=so)
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("to")
time.sleep(4)
step1 = driver.find_elements(By.XPATH,"//div[@class='products']/div")
for steps in step1:
    steps.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[text()='Apply']").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span[class='promoInfo']")))
m = driver.find_element(By.CSS_SELECTOR,"span[class='promoInfo']").text
#wait1 = FluentWait()
print(m)
assert m == "Code applied ..!"
driver.find_element(By.XPATH,"//div[@class='products']/div/button").click()
