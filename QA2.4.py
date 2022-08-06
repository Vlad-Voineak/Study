import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
def go(x):
    return math.log(abs(12 * math.sin(x)))
try:
    br=webdriver.Chrome()
    br.get('http://suninjuly.github.io/explicit_wait2.html')


    button = WebDriverWait(br, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'100')
    )

    br.find_element(By.CSS_SELECTOR, '#book').click()

    x= br.find_element(By.CSS_SELECTOR, '#input_value').text
    br.find_element(By.CSS_SELECTOR, '#answer').send_keys(go(int(x)))
    br.find_element(By.CSS_SELECTOR, '#solve').click()
finally:
    time.sleep(5)
    br.quit()

