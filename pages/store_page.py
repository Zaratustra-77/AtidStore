from selenium.webdriver.common.by import By
from .base_page import BasePage  # נניח שזה הנתיב של הקובץ
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class StorePage(BasePage):

    price_label_locator = (By.CSS_SELECTOR,"#woocommerce_price_filter-2 "
                                           "> form > div > div.price_slider_amount "
                                           "> div.price_label")
    price_from_locator = (By.CSS_SELECTOR,"#woocommerce_price_filter-2 "
                                          "> form > div > div.price_slider_amount "
                                          "> div.price_label > span.from")
    price_to_locator = (By.CSS_SELECTOR,"#woocommerce_price_filter-2 "
                                        "> form > div > div.price_slider_amount "
                                        "> div.price_label > span.to")
    filter_submit_btn = (By.CSS_SELECTOR, "#woocommerce_price_filter-2 "
                                          "> form > div > div.price_slider_amount "
                                          "> button")

    """Class to represent the login page actions."""

    left_slider_locator = (By.CSS_SELECTOR,"#woocommerce_price_filter-2 "
                                           "> form > div > div.price_slider."
                                           "ui-slider.ui-corner-all."
                                           "ui-slider-horizontal.ui-widget.ui-widget-content "
                                           "> span:nth-child(2)")
    right_slider_locator = (By.CSS_SELECTOR,"#woocommerce_price_filter-2 > form "
                                            "> div > div.price_slider.ui-slider."
                                            "ui-corner-all.ui-slider-horizontal."
                                            "ui-widget.ui-widget-content "
                                            "> span:nth-child(3)")

    base_url_store = "https://atid.store/store/"
    product_list_items_locator = (By.CSS_SELECTOR, "ul.products li.product")


    def enter_username(self, username):
        """Enters the username in the username field."""
        self.enter_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        """Enters the password in the password field."""
        self.enter_text(self.PASSWORD_FIELD, password)

    def login(self,username, password):
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)

    def click_login(self):
        """Clicks the login button."""
        self.click_element(self.LOGIN_BUTTON)

    def get_slider(self):
        slider = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#carouselExampleIndicators > div > div.carousel-item.active > img')))
        return slider

    def wait_for_carusel_image_change(self):
        slider = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#carouselExampleIndicators > div > div.carousel-item.active > img')))
        print(slider.get_attribute("src"))
        slider_src_attr = slider.get_attribute("src")
        while slider_src_attr == "https://www.demoblaze.com/Samsung1.jpg":
            slider_src_attr = slider.get_attribute("src")
        return slider_src_attr

    def menu_list_items(self):
        item_list = WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(("css selector", "#navbarExample")))
        print(item_list)
        return item_list