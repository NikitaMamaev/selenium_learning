from selenium import webdriver
import time
import unittest


def reg(url):
    bro = webdriver.Chrome()
    bro.get(url)

    bro.find_element_by_css_selector('input.first[required]').send_keys('Ivan')
    bro.find_element_by_css_selector(
        'input.second[required]').send_keys('Vvalenkov')
    bro.find_element_by_css_selector(
        'input.third[required]').send_keys('email@example.com')

    button = bro.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    welcome_text = bro.find_element_by_tag_name("h1").text
    bro.quit()
    return welcome_text


class TestFinal(unittest.TestCase):
    def test_registration1(self):
        self.assertEqual(reg("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "There is no welcome text!")

    def test_registration2(self):
        self.assertEqual(reg("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "There is no welcome text!")


if __name__ == "__main__":
    unittest.main()
