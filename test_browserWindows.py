from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import math


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()


def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()
    first_window = browser.current_window_handle
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, 'input_value')))
    elementInput_value = browser.find_element(By.ID, 'input_value').text
    elementAnswer = browser.find_element(By.ID, 'answer')
    elementAnswer.send_keys(calculate(elementInput_value))
    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()
finally:
    time.sleep(11)
    browser.quit()