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
driver.get("http:/www.rahulshettyacademy.com/dropdownsPractise")


driver.find_element(By.XPATH,"//input[@id='autosuggest']").send_keys("isr")
time.sleep(3)

countries = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a")


for country in countries:
    if country.text == "Israel":
        country.click()
        break





# Web page stay alive till i say so 
while True:
    pass