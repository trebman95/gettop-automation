from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# Start the browser
browser = webdriver.Chrome(service=Service(driver_path))

#Locators
browser.find_element(By.ID, 'username') #Username, login pop-up
browser.find_element(By.ID, 'password') #Password #login pop-up
browser.find_element(By.XPATH, "//label[@for='user_login']") #Username text above input field, forgot password
browser.find_element(By.XPATH, "//button[@value='Reset password]") #Reset password button
browser.find_element(By.XPATH, "//i[@class='icon-user']") #User icon (top right, next to cart)