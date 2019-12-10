import time
from selenium import webdriver

vm6_url = 'https://172.31.247.8/auth'
email = 'n.mamaev@ispsystem.com'
pswd = 'q1w2e3'

#def wait_by_css_selector(br, selector):
#    timeout = 10
#    while timeout != 0:
#        elements = br.find_elements_by_css_selector(selector)
#        if len(elements) == 0:
#            timeout -= 1
#        else:
#            return elements


def submit(br):
    submit = br.find_element_by_css_selector('button[type="submit"]')
    submit.click()
    time.sleep(2)


def main():
    try:
        browser =  webdriver.Chrome()
        browser.get(vm6_url)
        time.sleep(2)

        imput_email = browser.find_element_by_css_selector('.ispui-input')
        imput_email.send_keys(email)

        submit(browser)

        input_password = browser.find_element_by_css_selector('input.ispui-input')
        input_password.send_keys(pswd)

        submit(browser)
        time.sleep(7)


    finally:
        browser.quit()


if __name__ == '__main__':
        main()  