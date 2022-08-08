import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language:")


@pytest.fixture(scope="function")
def browser(request):
    b_n=request.config.getoption("browser_name")
    b_l = request.config.getoption("language")
    if b_n=="chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': b_l})
        browser = webdriver.Chrome(options=options)
    else:
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", b_l)
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    print("\nquit browser..")
    browser.quit()