from selenium import webdriver
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    bro = webdriver.Chrome()
    bro.get(link)

    bro.find_element_by_css_selector('input[name="firstname"]').send_keys('Ivan')
    bro.find_element_by_css_selector('input[name="lastname"]').send_keys('Vvalenkov')
    bro.find_element_by_css_selector('input[name="email"]').send_keys('email@example.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'paste_file.txt')
    bro.find_element_by_css_selector('input[id="file"]').send_keys(file_path)

    bro.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(15)
    bro.quit()
