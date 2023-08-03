import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
try:
    so = Service('C:/Users/prashant/Downloads/chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=so)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    new = Select(driver.find_element(By.CSS_SELECTOR,"select[id='page-menu']"))
    new.select_by_value('20')
    time.sleep(20)
except Exception as e:
    print(e)