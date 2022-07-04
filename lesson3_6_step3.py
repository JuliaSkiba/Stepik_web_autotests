import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestCorrectTime:
    @pytest.mark.parametrize('page', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
    def test_correct_time(self, browser, page):
        link = f"https://stepik.org/lesson/{page}/step/1/"
        browser.get(link)
        browser.implicitly_wait(20)
        answer = browser.find_element(By.CSS_SELECTOR, ".ember-text-area")
        answer.send_keys(str(math.log(int(time.time()))))
        browser.implicitly_wait(20)
        button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
        button.click()
        message = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
        assert "Correct!" in message.text, print (message.text)


