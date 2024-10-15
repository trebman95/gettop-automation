from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# Start the browser
browser = webdriver.Chrome(service=Service(driver_path))

browser.get('https://gettop.us/')

browser.find_element(By.XPATH,"//a[text()='Tablets' and @class='nav-top-link']").click() #Tablet top header

expected_result = 'HOME / TABLET'
actual_result = browser.find_element(By.XPATH,"//nav[contains(@class,'breadcrumbs')]").text

assert actual_result == expected_result, f'Error! {actual_result} does not match {expected_result}'
print('Test case passed')

#sleep(6)
browser.quit()