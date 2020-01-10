from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    bro = webdriver.Chrome()
    bro.get("http://suninjuly.github.io/selects1.html")
    # bro.get("http://suninjuly.github.io/selects2.html")

    x = int(bro.find_element_by_id('num1').text)
    y = int(bro.find_element_by_id('num2').text)

    s = x + y

    select = Select(bro.find_element_by_tag_name('select'))
    select.select_by_value(str(s))

    bro.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(15)
    bro.quit()
