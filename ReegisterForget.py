from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium_utils import safe_click
import time

# setting a service
serv = Service("C:/Users/seanp/Desktop/Self Improvement/Selenium Course - Python/chromedriver.exe")

# Chrome web browser 
driver = webdriver.Chrome(service = serv) # opening web browser
driver.minimize_window() # Maximize window 
driver.get("http:/www.rahulshettyacademy.com/client")



# Forgot password
safe_click(driver,By.LINK_TEXT, "Forgot password?")
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("321321321")
driver.find_element(By.XPATH, "//form/div[3]/input").send_keys("321321321")
safe_click(driver,By.XPATH, "//form/div[4]/button")

time.sleep(5)
# Login after forgot password
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("321321321")
safe_click(driver,By.XPATH, "//form/input")

driver.find_element(By.XPATH,"//*[@id='sidebar']/form/div[1]/input").send_keys("shoes")

while True:
    pass

# driver.find_element(By.ID, "firstName").send_keys("Sean")
# driver.find_element(By.ID, "lastName").send_keys("Mosses")

# driver.find_element(By.ID, "userMobile").send_keys("6543216654")

# driver.find_element(By.CLASS_NAME, "custom-select ng-valid ng-dirty ng-touched").click()



while True:
    pass
