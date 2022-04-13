import math
from selenium import webdriver
import time 

link = "http://suninjuly.github.io/wait1.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text
finally:
    # успеваем скопировать код за 30 секунд
    #time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()