import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name",
                     action="store",
                     default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language",
                     action="store",
                     default=None,
                     help="Choose language: ru, en, ... (etc.)")

#Chrome
#options = Options()
#options.add_experimental_option('prefs', {'intl.accept_languages': "language"})
# Firefox
#fp = webdriver.FirefoxProfile()
#fp.set_preference("intl.accept_languages", "language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name").lower()
    user_language = request.config.getoption("language").lower()    
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    print(f"\nStart {browser_name.capitalize()} browser for test...")
    yield browser
    print("\nQuit browser...")
    browser.quit()
