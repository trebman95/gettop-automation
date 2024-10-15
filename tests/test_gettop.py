from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#from time import sleep


class TestGetTop:

    def test_header_link_tablet(self):
        # Install and start the browser
        driver_path = ChromeDriverManager().install()
        browser = webdriver.Chrome(service=Service(driver_path))

        # Click 'Tablets' link on the homepage
        browser.get('https://gettop.us/')
        browser.find_element(By.XPATH, "//a[text()='Tablets' and @class='nav-top-link']").click()#Tablet top header

        #Verify correct page opens
        expected_result = 'HOME / TABLET'
        actual_result = browser.find_element(By.XPATH, "//nav[contains(@class,'breadcrumbs')]").text
        assert actual_result == expected_result

        browser.quit()