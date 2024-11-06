from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """Class to represent the base page that other pages can inherit from."""
    def __init__(self, driver: WebDriver):
        self.driver = driver
    def find_element(self, locator):
        """Finds element based on locator passed."""
        return WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """Clicks on element found by locator."""
        self.find_element(locator).click()
    def enter_text(self, locator, text):
        """Enters text in a specified field located by the locator."""
        element = self.find_element(locator)
        element.clear()  # Clear any existing text
        element.send_keys(text)
    def click_and_hold(self,element,xoffset,yoffset):
        actions = ActionChains(self.driver)
        actions.click_and_hold(element).move_by_offset(xoffset, yoffset=0).release().perform()  # 50 הוא הקיזוז האופקי לה

if __name__ == '__main__':
    # page=BasePage()
    pass