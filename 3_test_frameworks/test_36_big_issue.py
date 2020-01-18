from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import pytest
import time

links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


def get_answer():
    return math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', links)
class TestAlienFeedback():
    def test_issue(self, browser, link):
        browser.get(link)
        textarea = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea.textarea'))
        )
        textarea.send_keys(str(get_answer()))
        browser.find_element_by_css_selector(
            'button.submit-submission').click()

        response = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'pre'))
        )
        #response = browser.find_element_by_css_selector('pre')
        print(response.text)
        assert response.text == "Correct!", f'expected not "{response.text}"'
