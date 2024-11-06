import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FOP
from selenium.webdriver.chrome.options import Options as COP
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.firefox import GeckoDriverManager
# Set webdriver_manager to use the local cache
os.environ['WDM_LOCAL'] = '1'

@pytest.fixture(scope="function",params=["chrome","firefox"])
def driver(request):
    firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
    firefox_capabilities['timeouts'] = {"implicit": 120000, "pageLoad": 120000, "script": 30000}
    # browser = request.param
    selected_browser = request.config.getoption("--cmdopt")
    if selected_browser and selected_browser != request.param:
        pytest.skip(f"Skipping {request.param} because --cmdopt={selected_browser} is specified")

    browser = request.param
    driver = None

    if browser == "chrome":
        print(f"creating {browser} driver")
        """Fixture for setting up the WebDriver instance."""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_service = Service(ChromeDriverManager().install())  # Use the path directly
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")  # Recommended for CI environments
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.maximize_window()
        print(f"closing {browser} driver")
        yield driver
        driver.quit()


    elif browser == "firefox":
        print(f"Creating {browser} driver...")
        firefox_options = FOP()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_service = FireFoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
        driver.maximize_window()
        yield driver
        print(f"closing {browser} driver")
        driver.quit()
    else:
        raise TypeError(f"Expected 'Chrome' or 'Firefox' but got {browser}")

def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="chrome", help="browser options to execute tests (CHROME OR FIREFOX")