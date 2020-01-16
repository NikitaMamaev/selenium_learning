from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("button.btn").click()

    browser.switch_to.alert.accept()
    time.sleep(1)

    x = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(calc(x))

    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(15)
    browser.quit()