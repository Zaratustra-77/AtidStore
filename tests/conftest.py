import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FOP
from selenium.webdriver.chrome.options import Options as COP

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.firefox import GeckoDriverManager
# Set webdriver_manager to use the local cache
os.environ['WDM_LOCAL'] = '1'

@pytest.fixture(scope="function",params=["chrome","firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        print(f"creating {browser} driver")
        """Fixture for setting up the WebDriver instance."""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_service = Service(ChromeDriverManager().install())  # Use the path directly
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.maximize_window()
        print(f"closing {browser} driver")
        yield driver
        driver.quit()

    elif browser == "firefox":
        print(f"creating {browser} driver")
        firefoxService = FireFoxService(GeckoDriverManager().install())
        firefox_options = FOP()
        firefox_options.headless = True  # Enables private browsing mode
        driver = webdriver.Firefox(service=firefoxService,options=firefox_options)
        driver.maximize_window()
        yield driver
        print(f"closing {browser} driver")
        driver.quit()
    else:
        raise TypeError(f"Expected 'Chrome' or 'Firefox' but got {browser}")

def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="chrome", help="browser options to execute tests (CHROME OR FIREFOX")
