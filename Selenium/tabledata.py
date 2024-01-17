#table row and data for the xpath and css
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
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("a")
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

print(m)
list_of_total = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum =0
for list1 in list_of_total:
    sum = sum + int(list1.text)
dicountamount = float((10/100)*sum)
print(dicountamount)
final_re = float(sum - dicountamount)
result = driver.find_element(By.CSS_SELECTOR,"span[class='discountAmt']").text
print(result,final_re)
assert final_re == float(result)
