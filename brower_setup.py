import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

options = Options()
if os.getenv("CI"):  # GitHub Actions sets CI=true automatically
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

# Start the browser
driver = webdriver.Chrome(service=Service(driver_path), options=options)
browser = driver

#Locators
browser.find_element(By.ID, 'username') #Username, login pop-up
browser.find_element(By.ID, 'password') #Password #login pop-up
browser.find_element(By.XPATH, "//label[@for='user_login']") #Username text above input field, forgot password
browser.find_element(By.XPATH, "//button[@value='Reset password]") #Reset password button
browser.find_element(By.XPATH, "//i[@class='icon-user']") #User icon (top right, next to cart)
browser.find_element(By.ID,   'user_login') #Username input field
browser.find_element(By.XPATH, "//h1[text()='My Account']") #MY ACCOUNT text
browser.find_element(By.XPATH, "//a[text()='Accessories' and @class='nav-top-link']") #Accessories link in header
browser.find_element(By.XPATH, "//p[contains(text(),'Lost your password?')]" ) #“Lost your password…” text
browser.find_element(By.XPATH, "//ul[@id = 'menu-laptop-1']//a[text()='Accessories']") #Accessories link in footer

