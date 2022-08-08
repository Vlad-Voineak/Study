import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def go():
    return math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('lan', ["236895", "236896","236897","236898","236899","236903","236904","236905"])
def test1(browser,lan):
    link = f"https://stepik.org/lesson/{lan}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    at=browser.find_element(By.CSS_SELECTOR,'textarea')
    at.send_keys(go())
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    t=browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    assert t=='Correct!'