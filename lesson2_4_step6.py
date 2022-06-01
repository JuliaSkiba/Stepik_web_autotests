from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.ID, "button")

finally:
    time.sleep(10)
    browser.quit()