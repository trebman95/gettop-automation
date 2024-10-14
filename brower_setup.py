from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# Start the browser
browser = webdriver.Chrome(service=Service(driver_path))

#Locators
browser.find_element(By.ID, 'username')
browser.find_element(By.ID, 'password')
browser.find_element(By.XPATH, "//label[@for='user_login']")
browser.find_element(By.XPATH, "//button[@value='Reset password]")
browser.find_element(By.XPATH, "//i[@class='icon-user']")