from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    bro = webdriver.Chrome()
    bro.get("http://suninjuly.github.io/math.html")
    x = int(bro.find_element_by_id('input_value').text)
    y = calc(x)

    bro.find_element_by_id('answer').send_keys(y)
    bro.find_element_by_id('robotCheckbox').click()
    bro.find_element_by_id('robotsRule').click()

    bro.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    bro.quit()
