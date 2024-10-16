from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import pytest



class TestGetTop:
    browser = None

    def setup_method(self):
        # Install and start the browser
        driver_path = ChromeDriverManager().install()
        self.browser = webdriver.Chrome(service=Service(driver_path))

    def test_header_link_tablet(self):
        # Click 'Tablets' link on the homepage
        self.browser.get('https://gettop.us/')
        self.browser.find_element(By.XPATH, "//a[text()='Tablets' and @class='nav-top-link']").click()
        #Verify correct page opens
        expected_result = 'HOME / TABLET'
        actual_result = self.browser.find_element(By.XPATH, "//nav[contains(@class,'breadcrumbs')]").text
        assert actual_result == expected_result

    def test_empty_cart(self):
        # Click Cart icon on the homepage
        self.browser.get('https://gettop.us/')
        self.browser.find_element(By.XPATH, "//a[contains(@class,'header-cart-link is-small')]").click()
        sleep(3)
        #Verify that the empy cart message is displayed on the next page
        expected_result = 'Your cart is currently empty.'
        actual_result = self.browser.find_element(By.XPATH, "//p[text()='Your cart is currently empty.']").text
        assert actual_result == expected_result

    def test_profile_icon(self):
        # Click on user profile icon on the homepage (top right, next to cart)
        self.browser.get('https://gettop.us/')
        self.browser.find_element(By.XPATH, "//i[@class='icon-user']").click()
        sleep(3)
        #Verify that the empy cart message is displayed on the next page
        expected_result = 'LOGIN'
        actual_result = self.browser.find_element(By.XPATH, "//h3[text()='Login']").text
        assert actual_result == expected_result


    def test_product_search(self):
        # Search for thinkpad
        self.browser.get('https://gettop.us/')
        self.browser.find_element(By.XPATH, "//a[@aria-label='Search']").click()
        self.browser.find_element(By.ID, "woocommerce-product-search-field-0").send_keys('thinkpad', Keys.ENTER)
        # Verify search results are shown
        expected_text = 'HOME / SHOP / SEARCH RESULTS FOR “THINKPAD”'
        actual_text = self.browser.find_element(By.XPATH, "//nav[contains(@class, 'breadcrumbs')]").text
        assert actual_text == expected_text

        expected_product = 'ThinkPad'
        actual_product_title = self.browser.find_element(By.XPATH, "//p[@class='name product-title']").text
        assert expected_product in actual_product_title
        sleep(3)


    def teardown_method(self):
        self.browser.quit()