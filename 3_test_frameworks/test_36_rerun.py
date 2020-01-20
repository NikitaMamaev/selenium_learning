# pytest -v --tb=line --reruns 1 --browser_name=chrome 3_test_frameworks/test_36_rerun.py
# параметр "--tb=line", чтобы сократить лог с результатами теста
# "--reruns n", где n - это количество перезапусков

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")