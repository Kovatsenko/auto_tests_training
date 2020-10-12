from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import math


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()


def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    buttons = browser.find_elements(By.CSS_SELECTOR, 'button.btn')
    # elementPrice = browser.find_element(By.ID, 'price')
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    buttons[0].click()
    WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.ID, 'input_value')))
    elementInput_value = browser.find_element(By.ID, 'input_value').text
    elementAnswer = browser.find_element(By.ID, 'answer')
    elementAnswer.send_keys(calculate(elementInput_value))
    buttons[1].click()
finally:
    time.sleep(11)
    browser.quit()
