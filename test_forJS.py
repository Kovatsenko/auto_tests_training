from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

def calculate(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser.get(link)
    input_value = browser.find_element(By.ID, 'input_value').text
    answer = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(calculate(int(input_value)))
    robotCheckbox = browser.find_element(By.ID, 'robotCheckbox')
    robotCheckbox.click()
    robotsRule = browser.find_element(By.ID, 'robotsRule')
    robotsRule.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()
