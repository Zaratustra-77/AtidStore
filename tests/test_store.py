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
    product_list_items_element = sp.find_element(sp.product_list_items_locator)
    product_list_items_elements = product_list_items_element.find_elements()
    for item in product_list_items_elements:
        try:
            # Find the discounted price within each `<li>` item
            ins_tag = item.find_element(By.TAG_NAME,'ins')
            price = ins_tag.find_element(By.CSS_SELECTOR, 'span.woocommerce-Price-amount bdi').text
            print(f"Product sale Price: {price}")

        except Exception as e:
            print(f"Price not found in this item: {e}")

    time.sleep(5)  # המתנה קטנה כדי לראות את ההזזה

