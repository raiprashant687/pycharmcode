###############this is to handle java/javascript alerts sometimes shown on the browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

so = Service("C:/Users/prashant/Downloads/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=so)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("prashant")
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
al = driver.switch_to.alert
print(al.text)
al.accept()