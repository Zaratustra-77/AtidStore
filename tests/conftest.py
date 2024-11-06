import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FOP
from selenium.webdriver.chrome.options import Options as COP

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.firefox import GeckoDriverManager

# Set webdriver_manager to use the local cache
os.environ['WDM_LOCAL'] = '1'

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--cmdopt")
    driver = None

    if browser == "chrome":
        print(f"Creating {browser} driver...")
        chrome_options = COP()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")  # Recommended for CI environments
        chrome_service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    elif browser == "firefox":
        print(f"Creating {browser} driver...")
        firefox_options = FOP()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")  # Recommended for CI environments
        firefox_service = FireFoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

    else:
        raise TypeError(f"Expected 'chrome' or 'firefox' but got '{browser}'")

    driver.maximize_window()
    yield driver
    print(f"Closing {browser} driver...")
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="chrome", help="browser options to execute tests (chrome or firefox)"
    )
