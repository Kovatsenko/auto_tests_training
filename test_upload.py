from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    elementName = browser.find_element(By.NAME, 'firstname')
    elementName.send_keys('Ivan')
    elementLastName = browser.find_element(By.NAME, 'lastname')
    elementLastName.send_keys('Ivanov')
    elementMail = browser.find_element(By.NAME, 'email')
    elementMail.send_keys('mymail@mail.mail')
    directoryPath = os.path.dirname(os.path.dirname(__file__))
    filePath = os.path.join(directoryPath, 'Assets/Blank.txt')
    sendButton = browser.find_element(By.ID, 'file')
    sendButton.send_keys(filePath)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
finally:
    time.sleep(12)
    browser.quit()