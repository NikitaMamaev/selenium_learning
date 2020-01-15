from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    bro = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    bro.get(link)

    x = int(bro.find_element_by_id('input_value').text)
    y = calc(x)

    field = bro.find_element_by_id('answer')
    bro.execute_script("return arguments[0].scrollIntoView(true);", field)
    field.send_keys(y)

    chckbx = bro.find_element_by_id('robotCheckbox')
    bro.execute_script("return arguments[0].scrollIntoView(true);", chckbx)
    chckbx.click()

    rdbtn = bro.find_element_by_id('robotsRule')
    bro.execute_script("return arguments[0].scrollIntoView(true);", rdbtn)
    rdbtn.click()

    btn = bro.find_element_by_css_selector("button.btn")
    bro.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()

finally:
    time.sleep(15)
    bro.quit()