import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
try:
    so = Service('C:/Users/prashant/Downloads/chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=so)
    driver.maximize_window()
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
    window1 = driver.current_window_handle
    print(window1)
    s = driver.find_elements(By.CSS_SELECTOR,"a[class='increment']")
    for links in s:
        links.click()
    driver.find_element(By.CSS_SELECTOR,"a[class='cart-header-navlink']").click()
    window2=driver.current_window_handle
    print(driver.title)
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    new = Select(driver.find_element(By.CSS_SELECTOR,"select[id='page-menu']"))
    new.select_by_index(2)
    time.sleep(4)
    new1 = driver.find_element(By.CSS_SELECTOR,"input[type='search']")
    new1.click()
    new1.clear()
    new1.send_keys("tomato")
# print(driver.)
except Exception as e:
    print(e)

time.sleep(5)


