from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)

    y_element = browser.find_element(By.ID, "num2")
    y = int(y_element.text)

    summ = x+y
    Summ = str(summ)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(Summ)

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
