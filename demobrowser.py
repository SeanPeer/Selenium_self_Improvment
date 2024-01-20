from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# setting a service
serv = Service("C:/Users/seanp/Desktop/Self Improvement/Selenium Course - Python/chromedriver.exe")

# Chrome web browser 
driver = webdriver.Chrome(service = serv) # opening web browser
driver.maximize_window() # Maximize window 
driver.get("http:/www.ynet.co.il")
print(driver.title) # Prints web page title 
driver.current_url # In order to make sure that you are at the same url you wanted 

driver.get("http:/www.google.com")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()


driver.close()