import pytest
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from pages.store_page import StorePage as SP


@pytest.mark.home
def test_slider_filter_price_range_valid(driver):
    sp = SP(driver)
    driver.get(sp.base_url_store)
    slider_left = sp.find_element(SP.left_slider_locator)
    slider_right = sp.find_element(SP.right_slider_locator)
    # sp.click_and_hold(slider_left,10,0)
    time.sleep(2)
    sp.click_and_hold(slider_right,-200,0)
    price_to_element = sp.find_element(sp.price_to_locator)
    price_to_value = price_to_element.get_attribute("innerText")
    filter_submit_btn_element = sp.find_element(sp.filter_submit_btn)
    filter_submit_btn_element.click()
    carousell_element = sp.find_element(sp.carousell_element_locator)
    # carousell_elements = carousell_element.find_elements(sp.carouselle_inner_locator)
    # for item in carousell_elements:
    #     try:
    #         # Find the discounted price within each `<li>` item
    #         price_element = item.find_element(*SP.carouselle_inner_locator)
    #         price_text = price_element.text
    #
    #         # Extract and print the numeric part of the price
    #         price = float(price_text.split()[0])  # Convert to float if needed
    #         print(f"Discounted Price: {price}")
    #
    #     except Exception as e:
    #         print(f"Price not found in this item: {e}")

    time.sleep(5)  # המתנה קטנה כדי לראות את ההזזה

#
# //*[@id="main"]/div/ul/li[1]/div[2]/span[2]/span/bdi
# //*[@id="main"]/div/ul/li[2]/div[2]/span[2]/ins/span/bdi
# //*[@id="main"]/div/ul/li[3]/div[2]/span[2]/ins/span/bdi
# //*[@id="main"]/div/ul/li[2]/div[2]/span[2]/ins/span/bdi

# <bdi>45.00&nbsp;<span class="woocommerce-Price-currencySymbol">₪</span></bdi>