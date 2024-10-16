from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import pytest


class TestGetTop:
    browser = None

    def setup(self):
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
        #Verify that the empy cart message is displayed on the next page
        expected_result = 'Your cart is currently empty.'
        actual_result = self.browser.find_element(By.XPATH, "//p[text()='Your cart is currently empty.']").text
        assert actual_result == expected_result

    def test_login_form(self):
        # Click on user profile icon on the homepage (top right, next to cart)
        self.browser.get('https://gettop.us/')
        self.browser.find_element(By.XPATH, "//a[@class='nav-top-link nav-top-not-logged-in']").click()
        #Verify that the empy cart message is displayed on the next page
        expected_result = 'LOGIN'
        actual_result = self.browser.find_element(By.XPATH, "//h3[text()='Login']").text
        assert actual_result == expected_result


    def teardown(self):
        self.browser.quit()