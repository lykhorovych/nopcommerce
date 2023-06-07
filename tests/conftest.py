from random import choices

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from undetected_chromedriver import Chrome, ChromeOptions

from data.customer import Customer


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome')
    parser.addoption("--customers", action='store', default=1)


@pytest.fixture
def browser(request):
    if request.config.getoption("--browser"):
        return request.config.getoption("--browser")
    else:
        return 'chrome'


@pytest.fixture
def customer(request):
    return request.param


def pytest_generate_tests(metafunc):
    if 'customer' in metafunc.fixturenames:
        n = metafunc.config.getoption("--customers")
        metafunc.parametrize("customer", choices([Customer() for _ in range(int(100))], k=int(n)))


@pytest.fixture
def driver(request, browser):
    options = ChromeOptions()
    # proxy_server_url = "172.67.68.153"
    # options.add_argument(f'proxy-server={proxy_server_url}')
    # options.add_argument("--user-data-dir=C:\\Users\\Олег\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation", ])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                           {'source':
                                """
                                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol
                                """})
    # driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver


@pytest.fixture
def ud_driver(request):
    options = ChromeOptions()
    # options.add_argument('--headless')
    driver = Chrome(options=options, driver_executable_path='C:\\TOOLS\\chromedriver.exe')

    cdc_props = driver.execute_script('const j=[];for(const p in window){'
                                      'if(/^[a-z]{3}_[a-zA-Z0-9]{22}_.*/i.test(p)){'
                                      'j.push(p);delete window[p];}}return j;')
    if len(cdc_props) > 0:
        cdc_props_js_array = '[' + ','.join('"' + p + '"' for p in cdc_props) + ']'
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                               {'source': cdc_props_js_array + '.forEach(k=>delete window[k]);'})
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return driver


# Add hook to configure html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Oleh Lykhorovych'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop("Plugins", None)
